from model.local import Local
from view.local_tela import LocalTela

class LocalControlador:
    def __init__(self, sistema_controlador):
        self.__locais = []
        self.__sistema_controlador = sistema_controlador
        self.__tela = LocalTela()

    def _busca_local_por_nome_cidade(self, nome_cidade: str) -> Local | None:
        for local in self.__locais:
            if local.cidade.nome.lower() == nome_cidade.lower():
                return local
        return None

    def incluir_local(self):
        # Chama o 'cidade_controlador' a partir do 'sistema_controlador'
        self.__sistema_controlador.cidade_controlador.listar_cidades()
        
        nome_cidade = self.__tela.seleciona_cidade()
        cidade = self.__sistema_controlador.cidade_controlador._busca_cidade_por_nome(nome_cidade)

        if not cidade:
            self.__tela.mostra_mensagem("Erro: Cidade não encontrada!")
            return

        if self._busca_local_por_nome_cidade(nome_cidade):
            self.__tela.mostra_mensagem("Erro: Já existe um local cadastrado para esta cidade.")
            return

        novo_local = Local(cidade, [])
        self.__locais.append(novo_local)
        self.__tela.mostra_mensagem(f"Local para a cidade de {cidade.nome} criado com sucesso.")

    def listar_locais(self):
        if not self.__locais:
            self.__tela.mostra_mensagem("Nenhum local cadastrado.")
            return

        self.__tela.mostra_mensagem("\n--- LISTA DE LOCAIS ---")
        for local in self.__locais:
            dados_local = {
                "cidade": local.cidade.nome,
                "passeios": [p.nome for p in local.passeios]
            }
            self.__tela.mostra_local(dados_local)
        print("-----------------------")


    def excluir_local(self):
        self.listar_locais()
        if not self.__locais:
            return

        nome_cidade = self.__tela.seleciona_cidade()
        local = self._busca_local_por_nome_cidade(nome_cidade)

        if local:
            self.__locais.remove(local)
            self.__tela.mostra_mensagem("Local removido com sucesso.")
        else:
            self.__tela.mostra_mensagem("Erro: Local não encontrado.")

    def adicionar_passeio_a_local(self):
        self.listar_locais()
        if not self.__locais:
            return
        
        nome_cidade = self.__tela.seleciona_cidade()
        local = self._busca_local_por_nome_cidade(nome_cidade)

        if not local:
            self.__tela.mostra_mensagem("Erro: Local não encontrado.")
            return
        
        # Acessa o controlador de passeios a partir do sistema_controlador
        self.__sistema_controlador.passeio_turistico_controlador.listar_passeios()
        
        nome_passeio = self.__tela.seleciona_passeio()
        # Acessa o controlador de passeios a partir do sistema_controlador
        passeio = self.__sistema_controlador.passeio_turistico_controlador._busca_passeio_por_nome(nome_passeio)

        if not passeio:
            self.__tela.mostra_mensagem("Erro: Passeio não encontrado.")
            return
        
        if passeio in local.passeios:
            self.__tela.mostra_mensagem(f"O passeio '{passeio.nome}' já está associado a este local.")
            return

        local.passeios.append(passeio)
        self.__tela.mostra_mensagem(f"Passeio '{passeio.nome}' adicionado ao local de {local.cidade.nome}.")

    def retornar(self):
        self.__sistema_controlador.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_local,
            2: self.listar_locais,
            3: self.adicionar_passeio_a_local,
            4: self.excluir_local,
            0: self.retornar
        }
        while True:
            try:
                opcao = self.__tela.mostra_opcoes()
                lista_opcoes[opcao]()
            except (KeyError, ValueError):
                self.__tela.mostra_mensagem("Opção inválida, por favor, digite um número da lista.")
