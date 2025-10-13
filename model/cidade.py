from model.passeio_turistico import PasseioTuristico

class Cidade:
    def __init__(self, nome: str, passeios: list[PasseioTuristico] = None):
        self.__nome = None
        self.__passeios = []

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
    def passeios(self) -> list[PasseioTuristico]:
        return self.__passeios

    