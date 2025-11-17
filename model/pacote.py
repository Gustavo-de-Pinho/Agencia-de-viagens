from model.grupo import Grupo
from model.passagem import Passagem
from datetime import datetime

class Pacote:
    def __init__(self, grupo: Grupo, data: str):
        
        self.__grupo = None
        self.__passagens = []
        self.__valor_total = 0
        self.__valor_pago = 0
        self.__pago = False
        self.__data_viagem = self.converter_data(data)
        self.__itinerario = {}

        if isinstance(grupo, Grupo):
            self.__grupo = grupo

    def converter_data(self, data):
        try: 
            data = datetime.strptime(data, "%d-%m-%Y")
            return data
        except:
            return None

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

    @property
    def data_viagem(self):
        return self.__data_viagem
    
    @data_viagem.setter
    def data_viagem(self, data):
        self.__data_viagem = self.converter_data(data)

        