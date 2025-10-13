from model.grupo import Grupo
from model.passagem import Passagem
from model.local import Local

class Pacote:
    def __init__(self, grupo: Grupo):
        
        self.__grupo = None
        self.__passagens = []
        self.__valor_total = 0
        self.__valor_pago = 0
        self.__pago = False
        self.__itinerario = {}

        if isinstance(grupo, Grupo):
            self.__grupo = grupo

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

    @property
    def valor_pago(self):
        return self.__valor_pago
    
    @valor_pago.setter
    def valor_pago(self, valor):
        if isinstance(valor, float):
            self.__valor_pago = valor
    
    @property
    def pago(self):
        return self.__pago
    
    @pago.setter
    def pago(self, pago):
        if isinstance(pago, bool):
            self.__pago = pago