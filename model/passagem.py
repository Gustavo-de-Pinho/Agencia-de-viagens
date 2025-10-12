from model.pessoa import Pessoa
from model.transporte import Transporte
from model.cidade import Cidade

class Passagem:
    def __init__(self, pessoa: Pessoa, valor: float, transportes: Transporte, cidade_origem: Cidade, cidade_destino: Cidade):
        self.__pessoa = None
        self.__valor = 0.0
        self.__transportes = None
        self.__cidade_origem = None
        self.__cidade_destino = None

        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa
        if isinstance(valor, float):
            self.__valor = valor
        if isinstance(transportes, Transporte):
            self.__transportes = transportes
        if isinstance(cidade_origem, Cidade):
            self.__cidade_origem = cidade_origem
        if isinstance(cidade_destino, Cidade):
            self.__cidade_destino = cidade_destino

    @property
    def pessoa(self) -> Pessoa:
        return self.__pessoa
    
    @pessoa.setter
    def pessoa(self, pessoa: Pessoa):
        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa

    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float):
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def transportes(self) -> Transporte:
        return self.__transportes
    
    @transportes.setter
    def transportes(self, transportes: Transporte):
        if isinstance(transportes, Transporte):
            self.__transportes = transportes
    
    @property
    def cidade_origem(self) -> Cidade:
        return self.__cidade_origem
    
    @cidade_origem.setter
    def cidade_origem(self, cidade_origem: Cidade):
        if isinstance(cidade_origem, Cidade):
            self.__cidade_origem = cidade_origem
            
    @property
    def cidade_destino(self) -> Cidade:
        return self.__cidade_destino
    
    @cidade_destino.setter
    def cidade_destino(self, cidade_destino: Cidade):
        if isinstance(cidade_destino, Cidade):
            self.__cidade_destino = cidade_destino