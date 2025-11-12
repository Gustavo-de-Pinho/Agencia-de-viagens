from DAOs.dao import DAO
from model.cidade import Cidade

#cada entidade terá uma classe dessa, implementação bem simples.
class CidadeDAO(DAO):
    def __init__(self):
        super().__init__('cidade.pkl')

    def add(self, cidade: Cidade):
        if((cidade is not None) and isinstance(cidade, Cidade) and isinstance(cidade.nome, str)):
            super().add(cidade.nome, cidade)

    def update(self, cidade: Cidade):
        if((cidade is not None) and isinstance(cidade, Cidade) and isinstance(cidade.nome, str)):
            super().update(cidade.nome, cidade)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)