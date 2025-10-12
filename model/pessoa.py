from datetime import datetime

class Pessoa:
    def __init__(self, nome: str, data_nascimento: str, cpf: str, telefone: str):
        self.__nome = None
        self.__data_nascimento = None
        self.__cpf = None
        self.__telefone = None

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(data_nascimento, str):
            self.__data_nascimento = self.converter_data(data_nascimento)
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(telefone, str):
            self.__telefone = telefone

    def converter_data(self, data):
        try: 
            data = datetime.strptime(data, "%d-%m-%Y")
        except:
            data = None
        return data

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        if isinstance(data_nascimento, str):
            self.__data_nascimento = self.converter_data(data_nascimento)

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        if isinstance(telefone, str):
            self.__telefone = telefone