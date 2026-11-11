from datetime import date
from decimal import Decimal, InvalidOperation

from flask import Blueprint, jsonify, request, session

from .pais_dao import PaisDAO
from .visita import Visita
from .visita_dao import VisitaDAO


rotas_visitas = Blueprint("visitas", __name__, url_prefix="/api")

CAMPOS_TEXTO = {
    "cidade_principal": 100,
    "motivo_viagem": 60,
    "meio_transporte": 40,
    "observacao": 500,
    "moeda": 3,
}


def _ler_data(valor, campo, obrigatoria=False):
    if valor is None or valor == "":
        if obrigatoria:
            raise ValueError(f"Informe {campo}.")
        return None
    if not isinstance(valor, str):
        raise ValueError(f"Use AAAA-MM-DD em {campo}.")

    try:
        data = date.fromisoformat(valor)
    except ValueError:
        raise ValueError(f"Informe uma data válida em {campo} (AAAA-MM-DD).") from None
    if data.isoformat() != valor:
        raise ValueError(f"Use AAAA-MM-DD em {campo}.")
    return data


def _ler_texto_opcional(valor, campo, limite):
    if valor is None:
        return None
    if not isinstance(valor, str) or len(valor.strip()) > limite:
        raise ValueError(f"Use um texto de até {limite} caracteres em {campo}.")
    return valor.strip() or None


def _ler_avaliacao(valor):
    if valor is None or valor == "":
        return None

    mensagem = "Informe um número inteiro entre -128 e 127 em avaliacao."
    if isinstance(valor, bool) or not isinstance(valor, (int, str)):
        raise ValueError(mensagem)
    try:
        avaliacao = int(valor)
    except ValueError:
        raise ValueError(mensagem) from None
    if not -128 <= avaliacao <= 127:
        raise ValueError(mensagem)
    return avaliacao


def _ler_custo(valor):
    if valor is None or valor == "":
        return None

    mensagem = "Informe um custo de até oito dígitos inteiros e duas casas decimais."
    try:
        custo = Decimal(str(valor).replace(",", "."))
    except InvalidOperation:
        raise ValueError(mensagem) from None

    if not custo.is_finite() or custo.copy_abs() > Decimal("99999999.99"):
        raise ValueError(mensagem)
    custo_com_centavos = custo.quantize(Decimal("0.01"))
    if custo != custo_com_centavos:
        raise ValueError(mensagem)
    return custo_com_centavos


def _formatar_visita(linha):
    for campo in ("data_inicio", "data_fim", "criada_em", "atualizada_em"):
        valor = linha[campo]
        if isinstance(valor, date):
            linha[campo] = valor.isoformat()
    if linha["custo_estimado"] is not None:
        linha["custo_estimado"] = str(linha["custo_estimado"])
    return linha


@rotas_visitas.post("/visitas")
def cadastrar_visita():
    id_usuario = session.get("id_usuario")
    if id_usuario is None:
        return jsonify(erro="Entre na sua conta para registrar uma viagem."), 401

    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify(erro="Envie os dados da viagem em JSON."), 400

    codigo_mapa = dados.get("codigo_mapa")
    if not isinstance(codigo_mapa, str) or not codigo_mapa.strip():
        return jsonify(erro="Selecione um país ou território."), 400

    try:
        data_inicio = _ler_data(dados.get("data_inicio"), "data_inicio", obrigatoria=True)
        data_fim = _ler_data(dados.get("data_fim"), "data_fim")
        avaliacao = _ler_avaliacao(dados.get("avaliacao"))
        custo_estimado = _ler_custo(dados.get("custo_estimado"))
        textos = {
            campo: _ler_texto_opcional(dados.get(campo), campo, limite)
            for campo, limite in CAMPOS_TEXTO.items()
        }
    except ValueError as erro:
        return jsonify(erro=str(erro)), 400

    pais = PaisDAO().buscar_por_codigo_mapa(codigo_mapa.strip().upper())
    if pais is None:
        return jsonify(erro="Localidade não encontrada."), 404

    visita = Visita(
        id_usuario=id_usuario,
        id_pais=pais.id_pais,
        data_inicio=data_inicio,
        data_fim=data_fim,
        avaliacao=avaliacao,
        custo_estimado=custo_estimado,
        **textos,
    )
    if not visita.validarPeriodo():
        return jsonify(erro="A data de fim deve ser igual ou posterior à de início."), 400

    id_visita = VisitaDAO().cadastrar(visita)
    return jsonify(id_visita=id_visita, codigo_mapa=pais.codigo_mapa), 201


@rotas_visitas.get("/visitas")
def listar_visitas():
    id_usuario = session.get("id_usuario")
    if id_usuario is None:
        return jsonify(erro="Entre na sua conta para consultar suas viagens."), 401

    linhas = VisitaDAO().listar_por_usuario(id_usuario)
    return jsonify([_formatar_visita(linha) for linha in linhas])
