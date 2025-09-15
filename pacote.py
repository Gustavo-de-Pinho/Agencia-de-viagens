from grupo import Grupo
from passagem import Passagem
from local import Local

class Pacote:
    def __init__(self, grupo: Grupo, 
                 passagens: list[Passagem], 
                 valor_total: float, 
                 itinerario: list[Local]):
        
        self.__grupo = None
        self.__passagens = None
        self.__valor_total = None
        self.__itinerario = None

        if isinstance(grupo, Grupo):
            self.__grupo = grupo
        if isinstance(passagens, list):
            self.__passagens = passagens
        if isinstance(valor_total, float):
            self.__valor_total = valor_total
        if isinstance(itinerario, list):
            self.__itinerario = itinerario

    @property
    def grupo(self):
        return self.__grupo
    
    @grupo.setter
    def grupo(self, grupo):
        if isinstance(grupo, Grupo):
            self.__grupo = grupo

    @property
    def passagens(self):
        return self.__passagens
    
    @passagens.setter
    def passagens(self, passagens):
        if isinstance(passagens, list):
            self.__passagens = passagens

    @property
    def valor_total(self):
        return self.__valor_total
    
    @valor_total.setter
    def valor_total(self, valor_total):
        if isinstance(valor_total, float):
            self.__valor_total = valor_total

    @property
    def itinerario(self):
        return self.__itinerario
    
    @itinerario.setter
    def itinerario(self, itinerario):
        if isinstance(itinerario, list):
            self.__itinerario = itinerario