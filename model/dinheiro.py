from model.pagamento import Pagamento

class Dinheiro(Pagamento):
    def __init__(self, pessoa, grupo, valor):
        super().__init__(pessoa, grupo, valor)

