from .conexao import abrir_conexao
from .pais import Pais


class PaisDAO:
    def listar(self):
        with abrir_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM pais WHERE ativo = 1 ORDER BY nome")
                return [Pais(**linha) for linha in cursor.fetchall()]

    def buscar_por_codigo_mapa(self, codigo_mapa):
        with abrir_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM pais WHERE codigo_mapa = %s AND ativo = 1",
                    (codigo_mapa,),
                )
                linha = cursor.fetchone()
                return Pais(**linha) if linha is not None else None
