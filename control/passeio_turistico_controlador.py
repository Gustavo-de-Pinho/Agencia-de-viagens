from model.passeio_turistico import PasseioTuristico
from view.passeio_turistico_tela import PasseioTuristicoTela

class PasseioTuristicoControlador:
    def __init__(self, controlador_sistema):
        self.__passeios = []
        self.__controlador_sistema = controlador_sistema
        self.__tela = PasseioTuristicoTela()

    def _busca_passeio_por_nome(self, nome: str) -> PasseioTuristico | None:
        for p in self.__passeios:
            if p.nome == nome:
                return p
        return None

    def incluir_passeio(self):
        dados = self.__tela.pega_dados_passeio()
        
        if self._busca_passeio_por_nome(dados["nome"]):
            self.__tela.mostra_mensagem("Erro: Já existe um passeio com este nome!")
            return

        try:
            preco_float = float(dados["preco"])
            passeio = PasseioTuristico(dados["nome"], preco_float)
            self.__passeios.append(passeio)
            self.__tela.mostra_mensagem("Passeio cadastrado com sucesso!")
        except ValueError:
            self.__tela.mostra_mensagem("Erro: O preço informado é inválido.")

    def listar_passeios(self):
        if not self.__passeios:
            self.__tela.mostra_mensagem("Nenhum passeio turístico cadastrado.")
            return
        
        self.__tela.mostra_mensagem("\n--- LISTA DE PASSEIOS ---")
        for p in self.__passeios:
            self.__tela.mostra_passeio({"nome": p.nome, "preco": p.preco})
        print("------------------------")


    def alterar_passeio(self):
        self.listar_passeios()
        if not self.__passeios:
            return

        nome_passeio = self.__tela.seleciona_passeio()
        passeio = self._busca_passeio_por_nome(nome_passeio)

        if not passeio:
            self.__tela.mostra_mensagem("Passeio não encontrado.")
            return
        
        novos_dados = self.__tela.pega_dados_passeio()
        
        try:
            passeio.nome = novos_dados["nome"]
            passeio.preco = float(novos_dados["preco"])
            self.__tela.mostra_mensagem("Passeio alterado com sucesso.")
        except ValueError:
            self.__tela.mostra_mensagem("Erro: O preço informado é inválido.")

    def excluir_passeio(self):
        self.listar_passeios()
        if not self.__passeios:
            return

        nome_passeio = self.__tela.seleciona_passeio()
        passeio = self._busca_passeio_por_nome(nome_passeio)

        if not passeio:
            self.__tela.mostra_mensagem("Passeio não encontrado.")
            return
            
        self.__passeios.remove(passeio)
        self.__tela.mostra_mensagem("Passeio removido com sucesso.")

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_passeio,
            2: self.alterar_passeio,
            3: self.listar_passeios,
            4: self.excluir_passeio,
        }

        while True:
                opcao = self.__tela.mostra_opcoes()
                if opcao in lista_opcoes:
                    lista_opcoes[opcao]()
                elif opcao == 0:
                    break
                else:
                    self.__tela.mostra_mensagem("OPÇÃO INVÁLIDA")

