import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        self.__next_id = 0 

        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        data = {
            'cache': self.__cache,
            'next_id': self.__next_id
        }
        pickle.dump(data, open(self.__datasource, 'wb'))

    def __load(self):
        with open(self.__datasource,'rb') as file:
            data = pickle.load(file) 
            self.__cache = data.get('cache', {}) 
            self.__next_id = data.get('next_id', 0)

    def generate_next_id(self): 
        new_id = self.__next_id
        self.__next_id += 1
        return new_id
    
    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump()  

    def update(self, key, obj):
        try:
            if(self.__cache[key] != None):
                self.__cache[key] = obj 
                self.__dump()  
        except KeyError:
            pass  # implementar aqui o tratamento da exceção

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            pass #implementar aqui o tratamento da exceção
    
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump() 
        except KeyError:
            pass #implementar aqui o tratamento da exceção

    def get_all(self):
        return self.__cache.values()