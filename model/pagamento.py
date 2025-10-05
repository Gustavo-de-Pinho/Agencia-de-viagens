from model.pessoa import Pessoa
# HERDAR DE ABC (ABSTRATO)

class Pagamento:
    def __init__(self, pessoa: Pessoa, valor: float):
        self.__pessoa = None
        self.__valor = None

        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa
        if isinstance(valor, float):
            self.__valor = valor
    
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