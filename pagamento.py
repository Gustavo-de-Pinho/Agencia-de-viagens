from pessoa import Pessoa

class Pagamento:
    def __init__(self, pessoa: Pessoa, valor:float):
        self.__pessoa = None
        self.__valor = None

        if isinstance(pessoa, Pessoa):
            self.__pessoa = pessoa
        if isinstance(valor, float):
            self.__valor = valor
    