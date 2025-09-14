class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, telefone):
        self.__nome = None
        self.__data_nascimento = None
        self.__cpf = None
        self.__telefone = None

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(data_nascimento, int):
            self.__data_nascimento = data_nascimento
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(telefone, str):
            self.__telefone = str
