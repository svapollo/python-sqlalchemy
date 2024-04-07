from configs.connection import DBConnectionHandler
from src.entities.atores import Atores
from src.entities import Filmes


class AtoresRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session\
                .query(Atores)\
                .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                .with_entities(
                    Atores.nome,
                    Filmes.genero,
                    Filmes.titulo)\
                .all()
            return data
