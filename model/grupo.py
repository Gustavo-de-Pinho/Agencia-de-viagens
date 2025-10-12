class Grupo:
    def __init__(self, codigo: int):
        self.__codigo = None
        self.__membros = []

        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @property
    def membros(self):
        return self.__membros
    
