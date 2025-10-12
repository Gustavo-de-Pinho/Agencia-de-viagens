from model.pagamento import Pagamento

class CartaoCredito(Pagamento):
    def __init__(self, pessoa, valor, numero_cartao, bandeira):
        super().__init__(pessoa, valor)
        self.__numero_cartao = None
        self.__bandeira = None

        if isinstance(numero_cartao, str):
            self.__numero_cartao = numero_cartao
        if isinstance(bandeira, str):
            self.__bandeira = bandeira

    @property
    def numero_cartao(self):
        return self.__numero_cartao
        
    @numero_cartao.setter
    def numero_cartao(self, numero_cartao):
        if isinstance(numero_cartao, str):
            self.__numero_cartao = numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira
        
    @bandeira.setter
    def bandeira(self, bandeira):
        if isinstance(bandeira, str):
            self.__bandeira = bandeira