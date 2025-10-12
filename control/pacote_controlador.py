from model.pacote import Pacote
from view.pacote_tela import PacoteTela

class PacoteControlador:
    def __init__(self, sistema_controlador):
        self.__pacotes = []
        self.__tela = PacoteTela()
        self.__sistema_controlador = sistema_controlador

    #Checa se já existe um pacote ainda não pago ligado ao grupo
    def pacote_pendente(self, grupo):
        if grupo is not None:
            for pacote in self.__pacotes:
                if pacote.grupo == grupo:
                    if not pacote.pago:
                        return True #Já existe um pacote que não foi pago atrelado ao grupo
        return False

    def pacote_grupo(self, grupo):
        for pacote in self.__pacotes:
            if pacote.grupo == grupo and not pacote.pago:
                return pacote
        else:
            return None

    def criar_pacote(self):
        codigo = self.__tela.criar_pacote()
        grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(codigo)

        if grupo is not None and self.pacote_pendente(grupo):
            self.__pacotes.append(Pacote(grupo))
        else:
            self.__tela.mostrar_mensagem("GRUPO NÃO EXISTE OU JÁ HÁ UM PACOTE PENDENTE ATRELADO AO GRUPO")

    def adicionar_passagem(self):
        pacote = self.pacote_grupo(self.__tela.adicionar_passagem())

        if pacote is not None:
            passagem = self.__sistema_controlador.passagem_controlador.incluir_passagem()
            pacote.passagens.append(passagem)
            pacote.valor_total += passagem.valor
        else:
            self.__tela.mostrar_mensagem("PACOTE NÃO EXISTE")

    def criar_itinerario(self):
        grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo()
        dias = self.__tela.criar_itinerario()

        if dias is not None and grupo is not None:
            pacote = self.pacote_grupo(grupo)

            for dia in range(1, dias+1):
                dados = self.__tela.dia_itinerario(dia)

                cidade = self.__sistema_controlador.cidade_controlador._busca_pais_por_nome(dados["cidade"])
                passeio = self.__sistema_controlador.passeio_controlador._busca_passeio_por_nome(dados["passeio"])

                if cidade is not None:
                    pacote.itinerario[dia]["cidade"] = cidade
                if passeio is not None:
                    pacote.itinerario[dia]["passeio"] = passeio
                    pacote.valor_total += passeio.valor

    def historico_pacotes(self):
        codigo = self.__tela.historico_pacotes()
        
        if codigo is not None:
            grupo = self.__sistema_controlador.grupo_por_codigo(codigo)

            for pacote in self.__pacotes:
                if pacote.grupo == grupo:
                    valor_total = pacote.valor_total
                    passagens = []
                    itinerario = pacote.itinerario

                    for passagem in pacote.passagens:
                        pessoa = passagem.pessoa
                        cidade_origem = passagem.cidade_origem.nome
                        cidade_destino = passagem.cidade_destino.nome

                        passagens.append(f"{pessoa} | {cidade_origem} > {cidade_destino}")

                    self.__tela.mostrar_pacote({"valor_total": valor_total, "passagens": passagens, "itinerario": itinerario})

    def excluir_pacote(self):
        codigo = self.__tela.excluir_pacote()

        if codigo is not None:
            grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo()
            pacote = self.pacote_grupo(grupo)

            if pacote is not None:
                self.__pacotes.remove(pacote)

    def opcoes_editar_pacote(self):
        opcoes = {1: self.adicionar_passagem,
                  2: self.criar_itinerario}
        
        continua = True

        while continua:
            opcao = self.__tela.editar_pacote()

            if opcao in opcoes:
                opcoes[opcao]()
            elif opcao == 3:
                break
            else:
                self.__tela.mostrar_mensagem("OPÇÃO INVÁLIDA")

    def abre_tela(self):
        opcoes = {
            1: self.criar_pacote,
            2: self.opcoes_editar_pacote,
            3: self.historico_pacotes,
            4: self.excluir_pacote
        }

        continua = True

        while continua:
            opcao = self.__tela.opcoes()

            if opcao in opcoes:
                opcoes[opcao]()
            elif opcao == 5:
                break
            else:
                self.__tela.mostrar_mensagem("OPÇÃO INVÁLIDA")