import unittest
from secrets import token_hex
from uuid import uuid4

from backend.app import create_app
from backend.conexao import abrir_conexao


class TesteFluxo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app({"TESTING": True, "SECRET_KEY": token_hex(32)})

    def apagar_conta_de_teste(self, id_usuario):
        with abrir_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute("DELETE FROM visita WHERE id_usuario = %s", (id_usuario,))
                cursor.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
            conexao.commit()

    def cadastrar_conta(self, cliente):
        codigo = uuid4().hex
        dados = {
            "nome": "Conta de teste",
            "nome_usuario": f"teste_{codigo}",
            "email": f"{codigo}@passaporte.example",
            "senha": f"Viagem-{codigo}!",
        }
        resposta = cliente.post("/api/usuarios", json=dados)
        self.assertEqual(resposta.status_code, 201, resposta.get_json())
        id_usuario = resposta.get_json()["id_usuario"]
        self.addCleanup(self.apagar_conta_de_teste, id_usuario)
        self.assertNotIn("senha_hash", resposta.get_json())
        return dados

    def entrar(self, cliente, conta):
        resposta = cliente.post(
            "/api/login",
            json={"nome_usuario": conta["nome_usuario"], "senha": conta["senha"]},
        )
        self.assertEqual(resposta.status_code, 200, resposta.get_json())

    def test_listar_paises(self):
        cliente = self.app.test_client()
        self.assertEqual(cliente.get("/api/status").get_json(), {"status": "ok"})

        resposta = cliente.get("/api/paises")
        self.assertEqual(resposta.status_code, 200, resposta.get_json())
        paises = {pais["codigo_mapa"]: pais for pais in resposta.get_json()}
        self.assertEqual(len(paises), 13)
        self.assertEqual(paises["BRA"]["capital"], "Brasília")
        self.assertEqual(paises["GUF"]["tipo_localidade"], "TERRITORIO")

    def test_cadastrar_e_consultar_viagens_por_conta(self):
        cliente = self.app.test_client()
        outro_cliente = self.app.test_client()
        viagem = {"codigo_mapa": "BRA", "data_inicio": "2026-07-15"}

        self.assertEqual(cliente.get("/api/visitas").status_code, 401)
        self.assertEqual(cliente.post("/api/visitas", json=viagem).status_code, 401)

        conta = self.cadastrar_conta(cliente)
        segunda_conta = self.cadastrar_conta(outro_cliente)
        senha_errada = cliente.post(
            "/api/login",
            json={"nome_usuario": conta["nome_usuario"], "senha": "senha-incorreta"},
        )
        self.assertEqual(senha_errada.status_code, 401)
        self.entrar(cliente, conta)
        self.entrar(outro_cliente, segunda_conta)
        self.assertEqual(cliente.get("/api/visitas").get_json(), [])

        primeira = cliente.post("/api/visitas", json=viagem)
        self.assertEqual(primeira.status_code, 201, primeira.get_json())
        segunda = cliente.post(
            "/api/visitas",
            json={
                **viagem,
                "data_inicio": "2026-08-01",
                "data_fim": "2026-08-03",
                "cidade_principal": "Brasília",
                "motivo_viagem": "Turismo",
                "meio_transporte": "Ônibus",
                "avaliacao": "9",
                "observacao": "Visita de teste.",
                "custo_estimado": "125,50",
                "moeda": "BRL",
            },
        )
        self.assertEqual(segunda.status_code, 201, segunda.get_json())

        resposta = cliente.get("/api/visitas")
        self.assertEqual(resposta.status_code, 200, resposta.get_json())
        visitas = resposta.get_json()
        self.assertEqual(
            [visita["id_visita"] for visita in visitas],
            [segunda.get_json()["id_visita"], primeira.get_json()["id_visita"]],
        )
        self.assertEqual({visita["codigo_mapa"] for visita in visitas}, {"BRA"})
        self.assertEqual(visitas[0]["custo_estimado"], "125.50")
        self.assertEqual(visitas[0]["data_fim"], "2026-08-03")
        self.assertEqual(visitas[0]["avaliacao"], 9)
        self.assertIsNone(visitas[1]["data_fim"])

        resposta_outra_conta = outro_cliente.get("/api/visitas")
        self.assertEqual(resposta_outra_conta.status_code, 200)
        self.assertEqual(resposta_outra_conta.get_json(), [])
        self.assertEqual(cliente.post("/api/logout").status_code, 204)
        self.assertEqual(cliente.get("/api/visitas").status_code, 401)

    def test_rejeitar_viagens_invalidas(self):
        cliente = self.app.test_client()
        self.entrar(cliente, self.cadastrar_conta(cliente))
        viagem = {"codigo_mapa": "BRA", "data_inicio": "2026-07-15"}
        casos = [
            ({"data_inicio": ""}, 400),
            ({"data_inicio": "15/07/2026"}, 400),
            ({"data_fim": "2026-07-14"}, 400),
            ({"avaliacao": 1.5}, 400),
            ({"custo_estimado": "1.234"}, 400),
            ({"codigo_mapa": "INEXISTENTE"}, 404),
        ]
        for campos, codigo_esperado in casos:
            with self.subTest(campos=campos):
                resposta = cliente.post("/api/visitas", json={**viagem, **campos})
                self.assertEqual(resposta.status_code, codigo_esperado, resposta.get_json())
        self.assertEqual(cliente.get("/api/visitas").get_json(), [])

    def test_rejeitar_cadastro_duplicado(self):
        cliente = self.app.test_client()
        conta = self.cadastrar_conta(cliente)
        resposta = cliente.post("/api/usuarios", json=conta)
        self.assertEqual(resposta.status_code, 409, resposta.get_json())
