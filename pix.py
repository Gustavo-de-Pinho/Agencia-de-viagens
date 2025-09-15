from pagamento import Pagamento

class Pix(Pagamento):
    def __init__(self, pessoa, valor, cpf):
        super().__init__(pessoa, valor)
        self.__cpf = None

        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf