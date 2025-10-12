from model.cidade import Cidade
from model.passeio_turistico import PasseioTuristico

class Local:
    def __init__(self, cidade: Cidade, passeios: list[PasseioTuristico]):
        self.__cidade = None
        self.__passeios = []

        if isinstance(cidade, Cidade):
            self.__cidade = cidade
        
        if isinstance(passeios, list):
            self.__passeios = passeios

    @property
    def cidade(self) -> Cidade:
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade: Cidade):
        if isinstance(cidade, Cidade):
            self.__cidade = cidade

    @property
    def passeios(self) -> list[PasseioTuristico]:
        return self.__passeios