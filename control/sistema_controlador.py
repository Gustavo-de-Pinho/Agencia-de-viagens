from control.grupo_controlador import GrupoControlador
#from control.pacote_controlador import PacoteControlador
from control.pagamento_controlador import PagamentoControlador
from control.pessoa_controlador import PessoaControlador
from control.passagem_controlador import PassagemControlador

class SistemaControlador:
    def __init__(self):
        self.__grupo_controlador = GrupoControlador(self)
        #self.__pacote_controlador = PacoteControlador(self)
        self.__pagamento_controlador = PagamentoControlador(self)
        self.__pessoa_controlador = PessoaControlador(self)
        self.__passagem_controlador = PassagemControlador(self)

    @property
    def grupo_controlador(self):
        return self.__grupo_controlador
    
    #@property
    #def pacote_controlador(self):
        return self.__pacote_controlador
    
    @property
    def pagamento_controlador(self):
        return self.__pagamento_controlador
    
    @property
    def pessoa_controlador(self):
        return self.__pessoa_controlador
    
    @property
    def passagem_controlador(self):
        return self.__passagem_controlador

