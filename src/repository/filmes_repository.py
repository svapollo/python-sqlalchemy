from sqlalchemy.orm.exc import NoResultFound
from src.entities.filmes import Filmes


class FilmesRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler

    def select(self):
        with self.__ConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data

    def select_drama_filmes(self):
        with self.__ConnectionHandler() as db:
            try:
                data = db.session.query(Filmes).filter(Filmes=="kjljadj").one()
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                raise exception

    def insert(self, titulo, genero, ano):
        with self.__ConnectionHandler() as db:
            try:
                data_insert = Filmes(titulo=titulo,
                                     genero=genero,
                                     ano=ano)
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, titulo):
        with self.__ConnectionHandler() as db:
            db.session.query(Filmes).filter(
                Filmes.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano):
        with self.__ConnectionHandler() as db:
            db.session.query(Filmes).filter(
                Filmes.titulo == titulo).update(
                {"ano": ano})
            db.session.commit()
