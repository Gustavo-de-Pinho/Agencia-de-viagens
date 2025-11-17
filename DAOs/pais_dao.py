from DAOs.dao import DAO
from model.pais import Pais

class PaisDAO(DAO):
    def __init__(self):
        super().__init__('pais.pkl')

    def add(self, pais: Pais):
        if((pais is not None) and isinstance(pais, Pais) and isinstance(pais.nome, str)):
            novo_id = super().generate_next_id()
            pais.id = novo_id
            super().add(novo_id, pais)

    def update(self, pais: Pais):
        if((pais is not None) and isinstance(pais, Pais) and isinstance(pais.nome, str)):
            super().update(pais.id, pais)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)