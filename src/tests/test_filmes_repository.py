from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.entities.filmes import Filmes
from src.repository.filmes_repository import FilmesRepository


class ConnectionHandlerMock:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Filmes)],
                    [Filmes(titulo="Alice", genero="MMM", ano=12)]
                ),
                (
                    [
                        mock.call.query(Filmes),
                        mock.call.filter(Filmes.genero=="jajfjh")
                    ],
                    [Filmes(titulo="Apollo", genero="MMM", ano=12)]
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def test_select():
    filme_repository = FilmesRepository(ConnectionHandlerMock)
    response = filme_repository.select()
    print()
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], Filmes)


def test_select_drama_filmes():
    filme_repository = FilmesRepository(ConnectionHandlerMock)
    response = filme_repository.select_drama_filmes()
    print()
    print(response)
    assert isinstance(response, Filmes)
    assert response.titulo == "Alice"


def test_insert():
    filme_repository = FilmesRepository(ConnectionHandlerMock)
    response = filme_repository.insert("something", "AAAA", 33)
    print()
    print(response)
