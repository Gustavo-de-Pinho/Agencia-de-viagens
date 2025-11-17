from DAOs.dao import DAO
from model.grupo import Grupo


class GrupoDAO(DAO):
    def __init__(self):
        super().__init__("grupo.pkl")

    def add(self, grupo):
        if isinstance(grupo, Grupo) and isinstance(grupo.codigo, int):
            super().add(grupo.codigo, grupo)

    def update(self, grupo):
        if isinstance(grupo, Grupo) and isinstance(grupo.codigo, int):
            super().update(grupo.codigo, grupo)

    def get(self, codigo):
        if isinstance(codigo, int):
            return super().get(codigo)

    def remove(self, codigo):
        if isinstance(codigo, int):
            super().remove(codigo)
