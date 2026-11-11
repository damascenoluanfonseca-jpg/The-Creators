from config import abrir_conexao


class VisitaDAO:

    def cadastrar(self, visita):
        sql = """
            INSERT INTO visita (
                id_usuario,
                id_pais,
                data_inicio,
                data_fim,
                cidade_principal,
                motivo_viagem,
                meio_transporte,
                avaliacao,
                observacao,
                custo_estimado,
                moeda
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        parametros = (
            visita.id_usuario,
            visita.id_pais,
            visita.data_inicio,
            visita.data_fim,
            visita.cidade_principal,
            visita.motivo_viagem,
            visita.meio_transporte,
            visita.avaliacao,
            visita.observacao,
            visita.custo_estimado,
            visita.moeda
        )

        with abrir_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, parametros)
                id_visita = cursor.lastrowid

            conexao.commit()

        return id_visita

    def listar_por_usuario(self, id_usuario):
        sql = """
            SELECT
                visita.*,
                pais.codigo_mapa,
                pais.nome AS nome_pais
            FROM visita
            INNER JOIN pais
                ON pais.id_pais = visita.id_pais
            WHERE visita.id_usuario = %s
            ORDER BY
                visita.data_inicio DESC,
                visita.id_visita DESC
        """

        with abrir_conexao() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(sql, (id_usuario,))
                return cursor.fetchall()
