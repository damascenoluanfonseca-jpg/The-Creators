from flask import Blueprint, jsonify

from .pais_dao import PaisDAO


rotas_paises = Blueprint("paises", __name__, url_prefix="/api")


@rotas_paises.get("/paises")
def listar_paises():
    paises = PaisDAO().listar()
    return jsonify([pais.dados_mapa() for pais in paises])
