from cidade import Cidade
from passeio_turistico import PasseioTuristico

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
    
    def adicionar_passeio(self, passeios: PasseioTuristico):
        if isinstance(passeios, PasseioTuristico):
            self.__passeios.append(passeios)
            print(f"Passeio '{passeios.nome}' adicionado ao local.")
        else:
            print("Erro: O objeto a ser adicionado não é uma instância de PasseioTuristico.")