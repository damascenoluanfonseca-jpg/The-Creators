import os
from pathlib import Path

from flask import Flask, jsonify, render_template
from pymysql.err import MySQLError

from .rotas_paises import rotas_paises
from .rotas_usuarios import rotas_usuarios
from .rotas_visitas import rotas_visitas


PASTA_PROJETO = Path(__file__).resolve().parent.parent


def create_app(config=None):
    app = Flask(
        __name__,
        template_folder=str(PASTA_PROJETO / "pages"),
        static_folder=str(PASTA_PROJETO / "static"),
    )
    app.config.from_mapping(
        SECRET_KEY=os.getenv("FLASK_SECRET_KEY"),
        SESSION_COOKIE_SAMESITE="Lax",
    )
    if config is not None:
        app.config.update(config)
    if not app.config["SECRET_KEY"]:
        raise RuntimeError("Defina FLASK_SECRET_KEY no terminal antes de iniciar o Flask.")

    app.register_blueprint(rotas_paises)
    app.register_blueprint(rotas_usuarios)
    app.register_blueprint(rotas_visitas)

    @app.get("/")
    def inicio():
        if (PASTA_PROJETO / "pages" / "index.html").is_file():
            return render_template("index.html")
        return jsonify(mensagem="Passaporte Sul-Americano", status="/api/status")

    @app.get("/api/status")
    def status():
        return jsonify(status="ok")

    @app.errorhandler(MySQLError)
    def erro_banco(erro):
        app.logger.error("Falha em operação no MariaDB: %s", erro)
        return jsonify(erro="Falha ao consultar ou gravar no banco de dados."), 500

    return app
