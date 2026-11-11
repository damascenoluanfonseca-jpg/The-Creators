import re

from flask import Blueprint, jsonify, request, session
from pymysql.err import IntegrityError
from werkzeug.security import generate_password_hash

from .usuario import Usuario
from .usuario_dao import UsuarioDAO


rotas_usuarios = Blueprint("usuarios", __name__, url_prefix="/api")


@rotas_usuarios.post("/usuarios")
def cadastrar_usuario():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify(erro="Envie os dados da conta em JSON."), 400

    campos = {"nome": 100, "nome_usuario": 40, "email": 150}
    valores = {}
    for campo, limite in campos.items():
        valor = dados.get(campo)
        if not isinstance(valor, str) or not 1 <= len(valor.strip()) <= limite:
            return jsonify(erro=f"Preencha {campo} com até {limite} caracteres."), 400
        valores[campo] = valor.strip()

    email = valores["email"]
    if not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return jsonify(erro="Informe um e-mail válido."), 400

    senha = dados.get("senha")
    if not isinstance(senha, str) or not senha.strip():
        return jsonify(erro="Informe a senha."), 400

    usuario = Usuario(**valores, senha_hash=generate_password_hash(senha))
    try:
        usuario.id_usuario = UsuarioDAO().cadastrar(usuario)
    except IntegrityError as erro:
        if erro.args[0] != 1062:
            raise
        return jsonify(erro="Nome de usuário ou e-mail já cadastrado."), 409

    return jsonify(usuario.dados_publicos()), 201


@rotas_usuarios.post("/login")
def entrar():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict):
        return jsonify(erro="Envie o login em JSON."), 400

    nome_usuario = dados.get("nome_usuario")
    senha = dados.get("senha")
    if not isinstance(nome_usuario, str) or not nome_usuario.strip():
        return jsonify(erro="Informe o nome de usuário."), 400
    if not isinstance(senha, str) or not senha.strip():
        return jsonify(erro="Informe a senha."), 400

    dao = UsuarioDAO()
    usuario = dao.buscar_por_nome_usuario(nome_usuario.strip())
    if usuario is None or not usuario.ativo or not usuario.verificarSenha(senha):
        return jsonify(erro="Usuário ou senha inválidos."), 401

    dao.atualizar_ultimo_acesso(usuario.id_usuario)
    session.clear()
    session["id_usuario"] = usuario.id_usuario
    return jsonify(usuario.dados_publicos())


@rotas_usuarios.post("/logout")
def sair():
    session.clear()
    return "", 204
