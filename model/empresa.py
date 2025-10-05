class Empresa:
    def __init__(self, nome: str, cnpj: str):
        self.__nome = None
        self.__cnpj = None

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(cnpj, str):
            self.__cnpj = cnpj

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cnpj(self) -> str:
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj: str):
        if isinstance(cnpj, str):
            self.__cnpj = cnpj