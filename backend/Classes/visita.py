from .conexao import abrir_conexao


class Visita:
    def __init__(
        self,
        id_usuario,
        id_pais,
        data_inicio,
        data_fim=None,
        cidade_principal=None,
        motivo_viagem=None,
        meio_transporte=None,
        avaliacao=None,
        observacao=None,
        custo_estimado=None,
        moeda=None,
        id_visita=None,
        criada_em=None,
        atualizada_em=None,
    ):
        self.id_visita = id_visita
        self.id_usuario = id_usuario
        self.id_pais = id_pais
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.cidade_principal = cidade_principal
        self.motivo_viagem = motivo_viagem
        self.meio_transporte = meio_transporte
        self.avaliacao = avaliacao
        self.observacao = observacao
        self.custo_estimado = custo_estimado
        self.moeda = moeda
        self.criada_em = criada_em
        self.atualizada_em = atualizada_em

    def validar_periodo(self):
        return self.data_fim is None or self.data_fim >= self.data_inicio
