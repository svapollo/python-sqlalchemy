from src.repository.filmes_repository import FilmesRepository
from src.repository import AtoresRepository
from configs.connection import DBConnectionHandler

"""repo = FilmesRepository()
data = repo.select()
print(data)"""

repo_atores = AtoresRepository()
data_atores = repo_atores.select()
print(data_atores)

repo_filmes = FilmesRepository(DBConnectionHandler)
data_filmes_drama = repo_filmes.select_drama_filmes()
print(data_filmes_drama)
