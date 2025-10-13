from model.pagamento import Pagamento

class Pix(Pagamento):
    def __init__(self, pessoa, grupo, valor, cpf):
        super().__init__(pessoa, grupo, valor)
        self.__cpf_pagador = None

        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def cpf_pagador(self):
        return self.__cpf
    
    @cpf_pagador.setter
    def cpf_pagador(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf