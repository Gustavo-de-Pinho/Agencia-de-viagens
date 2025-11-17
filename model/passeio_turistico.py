class PasseioTuristico:
    def __init__(self, nome: str, id: int, preco: float):
        self.__nome = None
        self.__id = id
        self.__preco = 0

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
    def id(self):
        return self.__id

    @id.setter
    def id(self, novo_id: int):
        if isinstance(novo_id, int):
            self.__id = novo_id

    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, preco: float):
        if isinstance(preco, float):
            self.__preco = preco