from empresa import Empresa

class Transporte:
    def __init__(self, empresa: Empresa, meio_locomocao: str):
        self.__empresa = None
        self.__meio_locomocao = None

        if isinstance(empresa, Empresa):
            self.__empresa = empresa
        if isinstance(meio_locomocao, str):
            self.__meio_locomocao = meio_locomocao

    @property
    def empresa(self) -> Empresa:
        return self.__empresa
    
    @empresa.setter
    def empresa(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            self.__empresa = empresa

    @property
    def meio_locomocao(self) -> str:
        return self.__meio_locomocao
    
    @meio_locomocao.setter
    def meio_locomocao(self, meio_locomocao: str):
        if isinstance(meio_locomocao, str):
            self.__meio_locomocao = meio_locomocao