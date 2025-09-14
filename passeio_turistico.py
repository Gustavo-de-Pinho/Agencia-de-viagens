class PasseioTuristico:
    def __init__(self, nome: str, preco: float):
        self.__nome = None
        self.__float = 0

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(preco, float):
            self.__preco = preco

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, preco: float):
        if isinstance(preco, float):
            self.__nome = preco