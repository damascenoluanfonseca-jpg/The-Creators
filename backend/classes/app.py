from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
from pymysql.err import MySQLError
from werkzeug.exceptions import HTTPException

from backend.config import configuracao

from .rotas_paises import rotas_paises
from .rotas_usuarios import rotas_usuarios
from .rotas_visitas import rotas_visitas


PASTA_PROJETO = Path(__file__).resolve().parents[2]
PASTA_FRONTEND = PASTA_PROJETO / "frontend"


def create_app(config=None):
    app = Flask(
        __name__,
        static_folder=str(PASTA_FRONTEND),
        static_url_path="",
    )

    app.config.from_mapping(configuracao())

    if config is not None:
        app.config.update(config)

    if not app.config["SECRET_KEY"]:
        raise RuntimeError(
            "Defina FLASK_SECRET_KEY no terminal antes de iniciar o Flask."
        )

    app.register_blueprint(rotas_paises)
    app.register_blueprint(rotas_usuarios)
    app.register_blueprint(rotas_visitas)

    @app.before_request
    def conferir_origem():
        if request.path.startswith("/api/") and request.method in {
            "POST", "PUT", "PATCH", "DELETE"
        }:
            origem = request.headers.get("Origin")

            if origem and origem != request.host_url.rstrip("/"):
                return jsonify(
                    erro="Envie a requisição pela própria página do sistema."
                ), 403

    @app.after_request
    def configurar_resposta(resposta):
        resposta.headers["X-Content-Type-Options"] = "nosniff"

        if request.path.startswith("/api/"):
            resposta.headers["Cache-Control"] = "no-store"

        return resposta

    @app.get("/")
    @app.get("/index.html")
    def inicio():
        return send_from_directory(PASTA_PROJETO, "index.html")

    @app.get("/frontend/<path:arquivo>")
    def arquivos_frontend(arquivo):
        return send_from_directory(PASTA_FRONTEND, arquivo)

    @app.get("/api/status")
    def status():
        return jsonify(status="ok")

    @app.errorhandler(MySQLError)
    def erro_banco(erro):
        app.logger.error("Falha em operação no banco: %s", erro)

        return jsonify(
            erro="Falha ao consultar ou gravar no banco de dados."
        ), 500

    @app.errorhandler(HTTPException)
    def erro_http(erro):
        if request.path.startswith("/api/"):
            return jsonify(erro=erro.description), erro.code

        return erro

    return app
