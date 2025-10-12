from control.grupo_controlador import GrupoControlador
#from control.pacote_controlador import PacoteControlador
#rom control.pagamento_controlador import PagamentoControlador
from control.pessoa_controlador import PessoaControlador
#from control.passagem_controlador import PassagemController
from control.transporte_controlador import TransporteControlador

class SistemaControlador:
    def __init__(self):
        self.__grupo_controlador = GrupoControlador(self)
        #self.__pacote_controlador = PacoteControlador(self)
        #self.__pagamento_controlador = PagamentoControlador(self)
        self.__pessoa_controlador = PessoaControlador(self)
        #self.__passagem_controlador = PassagemController(self)
        self.__transporte_controlador = TransporteControlador(self)

    @property
    def grupo_controlador(self):
        return self.__grupo_controlador
    
    #@property
    #def pacote_controlador(self):
        return self.__pacote_controlador
    
    #@property
    #def pagamento_controlador(self):
        return self.__pagamento_controlador
    
    @property
    def pessoa_controlador(self):
        return self.__pessoa_controlador
    
    #@property
    #def passagem_controlador(self):
        return self.__passagem_controlador
    
    @property
    def transporte_controlador(self):
        return self.__transporte_controlador
    
