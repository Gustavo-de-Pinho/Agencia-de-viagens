from model.pacote import Pacote
from view.pacote_tela import PacoteTela
from DAOs.pacote_dao import PacoteDAO


class PacoteControlador:
    def __init__(self, sistema_controlador):
        self.__pacote_DAO = PacoteDAO()
        self.__tela = PacoteTela()
        self.__sistema_controlador = sistema_controlador

    #Checa se já existe um pacote ainda não pago ligado ao grupo
    def pacote_pendente(self, grupo):
        if grupo is not None:
            for pacote in self.__pacote_DAO.get_all():
                if pacote.grupo == grupo:
                    if not pacote.pago:
                        return True #Já existe um pacote que não foi pago atrelado ao grupo
        return False

    def pacote_grupo(self, grupo):
        for pacote in self.__pacote_DAO.get_all():
            if pacote.grupo == grupo and not pacote.pago:
                return pacote
        else:
            return None

    def criar_pacote(self):
        dados = self.__tela.criar_pacote()
        grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(dados["codigo"])
        data = dados["data"]
    
        pacote = Pacote(grupo, data)

        if grupo is not None and not self.pacote_pendente(grupo) and pacote.data_viagem is not None:
            self.__pacote_DAO.add(pacote)
        else:
            self.__tela.mostrar_mensagem("DADOS INVÁLIDOS")

    def adicionar_passagem(self):
        codigo = self.__tela.adicionar_passagem()
        grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(codigo)
        pacote = self.pacote_grupo(grupo)

        if pacote is not None:
            passagem = self.__sistema_controlador.passagem_controlador.incluir_passagem()
            
            if passagem is not None:
                pacote.passagens.append(passagem)
                pacote.valor_total += passagem.valor
                self.__tela.mostrar_mensagem("Passagem adicionada com sucesso.")
            else:
                self.__tela.mostrar_mensagem("ERRO: Falha ao criar a passagem. Verifique os dados.")
                
        else:
            self.__tela.mostrar_mensagem("PACOTE NÃO EXISTE")

    def criar_itinerario(self):
        dados = self.__tela.criar_itinerario()

        if dados is not None:
            grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(dados["codigo"])
            dias = dados["dias"]

        if dias is not None and grupo is not None:
            pacote = self.pacote_grupo(grupo)

            for dia in range(1, dias+1):
                dados2 = self.__tela.dia_itinerario(dia)
                pacote.itinerario[dia] = {}

                cidade = self.__sistema_controlador.cidade_controlador._busca_cidade_por_nome(dados2["cidade"])
                passeio = self.__sistema_controlador.passeio_turistico_controlador._busca_passeio_por_nome(dados2["passeio"])

                if cidade is not None:
                    pacote.itinerario[dia]["cidade"] = cidade
                if passeio is not None:
                    pacote.itinerario[dia]["passeio"] = passeio
                    pacote.valor_total += passeio.preco

    def historico_pacotes(self):
        codigo = self.__tela.historico_pacotes()
        
        if codigo is not None:

            for pacote in self.__pacote_DAO.get_all():
                if pacote.grupo.codigo == codigo:
                    valor_total = pacote.valor_total
                    valor_pago = pacote.valor_pago
                    pago = pacote.pago
                    passagens = []
                    itinerario = []

                    for passagem in pacote.passagens:
                        pessoa = passagem.pessoa.nome
                        cidade_origem = passagem.cidade_origem.nome
                        cidade_destino = passagem.cidade_destino.nome

                        passagens.append(f"{pessoa} | {cidade_origem} > {cidade_destino}")

                    for key in pacote.itinerario:
                        dia = key
                        cidade = "Não registrado"
                        passeio = "Não registrado"

                        if "cidade" in pacote.itinerario[key]:
                            cidade = pacote.itinerario[key]["cidade"].nome
                        if "passeio" in pacote.itinerario[key]:
                            passeio = pacote.itinerario[key]["passeio"].nome

                        itinerario.append(f"Dia {dia}: {cidade} | {passeio}")

                    self.__tela.mostrar_pacote({"valor_total": valor_total, "passagens": passagens, "itinerario": itinerario, "valor_pago": valor_pago, "pago": pago})

    def excluir_pacote(self):
        codigo = self.__tela.excluir_pacote()

        if codigo is not None:
            grupo = self.__sistema_controlador.grupo_controlador.grupo_por_codigo(codigo)
            pacote = self.pacote_grupo(grupo)

            if pacote is not None:
                self.__pacote_DAO.remove(pacote)

    def opcoes_editar_pacote(self):
        opcoes = {1: self.adicionar_passagem,
                  2: self.criar_itinerario}
        
        continua = True

        while continua:
            opcao = self.__tela.editar_pacote()

            if opcao in opcoes:
                opcoes[opcao]()
            elif opcao == 0:
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
            elif opcao == 0:
                break
            else:
                self.__tela.mostrar_mensagem("OPÇÃO INVÁLIDA")