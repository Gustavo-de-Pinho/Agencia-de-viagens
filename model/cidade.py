from model.passeio_turistico import PasseioTuristico

class Cidade:
    def __init__(self, nome: str, id: int = None, passeios: list[PasseioTuristico] = None):
        self.__nome = None
        self.__id = id
        self.__passeios = []
        self.__visitas = 0

        if isinstance(nome, str):
            self.__nome = nome
    
        if isinstance(passeios, list):
            self.__passeios = passeios
        
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
    def passeios(self) -> list[PasseioTuristico]:
        return self.__passeios
    
    @property
    def visitas(self):
        return self.__visitas
    
    @visitas.setter
    def visitas(self, visitas):
        if isinstance(visitas, int):
            self.__visitas = visitas

    