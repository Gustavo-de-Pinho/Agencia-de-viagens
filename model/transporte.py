from model.empresa import Empresa

class Transporte:
    def __init__(self, empresa: Empresa, id: int, meio_locomocao: str):
        self.__empresa = None
        self.__id = id
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
    def id(self):
        return self.__id

    @id.setter
    def id(self, novo_id: int):
        if isinstance(novo_id, int):
            self.__id = novo_id

    @property
    def meio_locomocao(self) -> str:
        return self.__meio_locomocao
    
    @meio_locomocao.setter
    def meio_locomocao(self, meio_locomocao: str):
        if isinstance(meio_locomocao, str):
            self.__meio_locomocao = meio_locomocao