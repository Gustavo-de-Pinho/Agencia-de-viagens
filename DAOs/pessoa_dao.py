import pickle
from model.pessoa import Pessoa
from DAOs.dao import DAO


class PessoaDAO(DAO):
    def __init__(self):
        super().__init__("pessoa.pkl")

    def add(self, pessoa):
        if isinstance(pessoa, Pessoa) and isinstance(pessoa.cpf, str):
            cpf = pessoa.cpf
            super().add(cpf, pessoa)

    def update(self, pessoa):
        if isinstance(pessoa, Pessoa) and isinstance(pessoa.cpf, str):
            super().update(pessoa.cpf, pessoa)

    def remove(self, cpf):
        if isinstance(cpf, str):
            super().remove(cpf)

    def get(self, cpf):
        if isinstance(cpf, str):
            super().get(cpf)
