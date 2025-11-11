from DAOs.dao import DAO
from model.pais import Pais

#cada entidade terá uma classe dessa, implementação bem simples.
class PaisDAO(DAO):
    def __init__(self):
        super().__init__('pais.pkl')

    def add(self, pais: Pais):
        if((pais is not None) and isinstance(pais, Pais) and isinstance(pais.nome, str)):
            super().add(pais.nome, pais)

    def update(self, pais: Pais):
        if((pais is not None) and isinstance(pais, Pais) and isinstance(pais.nome, str)):
            super().update(pais.nome, pais)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)