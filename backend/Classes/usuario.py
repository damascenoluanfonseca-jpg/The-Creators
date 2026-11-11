from werkzeug.security import check_password_hash


class Usuario:
    def __init__(
        self,
        nome,
        nome_usuario,
        email,
        senha_hash,
        id_usuario=None,
        foto_perfil_url=None,
        biografia=None,
        data_cadastro=None,
        ultimo_acesso=None,
        ativo=True,
    ):
        self.id_usuario = id_usuario
        self.nome = nome
        self.nome_usuario = nome_usuario
        self.email = email
        self.senha_hash = senha_hash
        self.foto_perfil_url = foto_perfil_url
        self.biografia = biografia
        self.data_cadastro = data_cadastro
        self.ultimo_acesso = ultimo_acesso
        self.ativo = bool(ativo)

    def verificarSenha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def dados_publicos(self):
        return {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "nome_usuario": self.nome_usuario,
        }
