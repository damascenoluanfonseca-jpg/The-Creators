class Pais:

    def __init__(self, id_pais, nome, codigo_mapa, codigo_iso2, codigo_iso3, capital, tipo_localidade, latitude_referencia, longitude_referencia, bandeira_url, cadastrado_em, ativo ):
        self.id_pais = id_pais
        self.nome = nome
        self.codigo_mapa = codigo_mapa
        self.codigo_iso2 = codigo_iso2
        self.codigo_iso3 = codigo_iso3
        self.capital = capital
        self.tipo_localidade = tipo_localidade
        self.latitude_referencia = latitude_referencia
        self.longitude_referencia = longitude_referencia
        self.bandeira_url = bandeira_url
        self.cadastrado_em = cadastrado_em
        self.ativo = ativo
    def ehTerritorio(self):
        return self.tipo_localidade == "TERRITORIO"

    def dados_mapa(self):
        return {
            "id_pais": self.id_pais,
            "nome": self.nome,
            "codigo_mapa": self.codigo_mapa,
            "codigo_iso2": self.codigo_iso2,
            "codigo_iso3": self.codigo_iso3,
            "capital": self.capital,
            "tipo_localidade": self.tipo_localidade,
            "latitude_referencia": (
                float(self.latitude_referencia)
                if self.latitude_referencia is not None else None
            ),
            "longitude_referencia": (
                float(self.longitude_referencia)
                if self.longitude_referencia is not None else None
            ),
            "bandeira_url": self.bandeira_url,
        }
