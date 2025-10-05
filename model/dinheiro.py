from model.pagamento import Pagamento

class Dinheiro(Pagamento):
    def __init__(self, pessoa, valor):
        super().__init__(pessoa, valor)

