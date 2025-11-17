from model.pessoa import Pessoa
from model.grupo import Grupo
# HERDAR DE ABC (ABSTRATO)

class Pagamento:
    def __init__(self, pessoa: Pessoa, grupo: Grupo, valor: float):
        self.__id = 0
        self.__pessoa = None
        self.__grupo = None
        self.__valor = None

        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa
        if isinstance(valor, float):
            self.__valor = valor
        if isinstance(grupo, Grupo):
            self.__grupo = grupo
    
    @property
    def pessoa(self):
        return self.__pessoa
    
    @pessoa.setter
    def pessoa(self, pessoa):
        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def grupo(self):
        return self.__grupo
    
    @grupo.setter
    def grupo(self, grupo):
        if isinstance(grupo, Grupo):
            self.__grupo = grupo