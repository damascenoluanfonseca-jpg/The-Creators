from .conexao import abrir_conexao
from .usuario import Usuario


class UsuarioDAO:
    def cadastrar(self, usuario):
        sql = """
            INSERT INTO usuario (nome, nome_usuario, email, senha_hash)
            VALUES (%s, %s, %s, %s)
        """
        parametros = (
            usuario.nome,
            usuario.nome_usuario,
            usuario.email,
            usuario.senha_hash,
        )

        with abrir_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, parametros)
                id_usuario = cursor.lastrowid
            conexao.commit()
        return id_usuario

    def buscar_por_nome_usuario(self, nome_usuario):
        with abrir_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM usuario WHERE nome_usuario = %s",
                    (nome_usuario,),
                )
                linha = cursor.fetchone()
                return Usuario(**linha) if linha is not None else None

    def atualizar_ultimo_acesso(self, id_usuario):
        with abrir_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE usuario SET ultimo_acesso = CURRENT_TIMESTAMP()
                    WHERE id_usuario = %s
                    """,
                    (id_usuario,),
                )
            conexao.commit()

