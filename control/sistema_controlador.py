from control.grupo_controlador import GrupoControlador
from control.pagamento_controlador import PagamentoControlador
from control.pessoa_controlador import PessoaControlador
from control.transporte_controlador import TransporteControlador
from control.passeio_turistico_controlador import PasseioTuristicoControlador
from control.cidade_controlador import CidadeControlador
from control.passagem_controlador import PassagemControlador
from control.pacote_controlador import PacoteControlador
from view.sistema_tela import SistemaTela


class SistemaControlador:
    def __init__(self):
        self.__tela = SistemaTela()
        self.__grupo_controlador = GrupoControlador(self)
        self.__pagamento_controlador = PagamentoControlador(self)
        self.__pessoa_controlador = PessoaControlador(self)
        self.__transporte_controlador = TransporteControlador(self)
        self.__passeio_turistico_controlador = PasseioTuristicoControlador(self)
        self.__cidade_controlador = CidadeControlador(self)
        self.__passagem_controlador = PassagemControlador(self)
        self.__pacote_controlador = PacoteControlador(self)

    def gerar_relatorio(self):
        self.__tela.gerar_relatorio({
            "pessoas": len(self.__pessoa_controlador.pessoas),
            "grupos": len(self.__grupo_controlador.grupos),
            "cidades": len(self.__cidade_controlador.cidades),
            "paises": len(self.__cidade_controlador.paises),
            "passeios_turisticos": len(self.__passeio_turistico_controlador.passeios)
        })

    def abre_tela(self):
        opcoes = {
            1: self.__pessoa_controlador.abre_tela,
            2: self.__grupo_controlador.abre_tela,
            3: self.__cidade_controlador.abre_tela,
            4: self.passeio_turistico_controlador.abre_tela,
            5: self.transporte_controlador.abre_tela,
            6: self.__pacote_controlador.abre_tela,
            7: self.__pagamento_controlador.abre_tela,
            8: self.gerar_relatorio
        }

        continua = True

        while continua:
            opcao = self.__tela.tela_opcoes()

            if opcao in opcoes:
                opcoes[opcao]()
            elif opcao == 0:
                break
            else:
                self.__tela.mostrar_mensagem("CÓDIGO INVÁLIDO")

    @property
    def grupo_controlador(self):
        return self.__grupo_controlador
    
    @property
    def pacote_controlador(self):
        return self.__pacote_controlador
    
    @property
    def pagamento_controlador(self):
        return self.__pagamento_controlador
    
    @property
    def pessoa_controlador(self):
        return self.__pessoa_controlador
    
    @property
    def transporte_controlador(self):
        return self.__transporte_controlador
    
    @property
    def passeio_turistico_controlador(self):
        return self.__passeio_turistico_controlador
    
    @property
    def cidade_controlador(self):
        return self.__cidade_controlador
    
    @property
    def local_controlador(self):
        return self.__local_controlador
    
    @property
    def passagem_controlador(self):
        return self.__passagem_controlador
