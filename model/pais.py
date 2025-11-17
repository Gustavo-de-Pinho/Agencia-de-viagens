from model.cidade import Cidade

class Pais:
    def __init__(self, nome: str, id: int = None, cidades: list[Cidade] = None):
        self.__nome = None
        self.__id = id
        self.__cidades = []

        if isinstance(nome, str):
            self.__nome = nome
    
        if cidades is not None:
            if isinstance(cidades, list):
                self.__cidades = cidades

        @property
        def id(self):
            return self.__id

        @id.setter
        def id(self, novo_id: int):
            if isinstance(novo_id, int):
                self.__id = novo_id
        
    def adicionar_cidade(self, cidade):
        if isinstance(cidade, Cidade):
            self.__cidades.append(cidade)
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def cidades(self) -> list[Cidade]:
        return self.__cidades