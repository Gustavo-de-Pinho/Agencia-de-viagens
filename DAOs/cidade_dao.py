from DAOs.dao import DAO
from model.cidade import Cidade


class CidadeDAO(DAO):
    def __init__(self):
        super().__init__('cidade.pkl')

    def add(self, cidade: Cidade):
        if((cidade is not None) and isinstance(cidade, Cidade) and isinstance(cidade.nome, str)):
            novo_id = super().generate_next_id()
            cidade.id = novo_id
            super().add(novo_id, cidade)

    def update(self, cidade: Cidade):
        if((cidade is not None) and isinstance(cidade, Cidade) and isinstance(cidade.nome, str)):
            super().update(cidade.id, cidade)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)