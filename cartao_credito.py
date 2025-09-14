from pagamento import Pagamento

class CartaoCredito(Pagamento):
    def __init__(self, pessoa, valor, numero_cartao, bandeira):
        super().__init__(pessoa, valor)
        self.__numero_cartao = None
        self.__bandeira = None

        if isinstance(numero_cartao, int):
            self.__numero_cartao = numero_cartao
        if isinstance(bandeira, str):
            self.__bandeira = bandeira

            