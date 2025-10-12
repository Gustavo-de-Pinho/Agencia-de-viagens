from model.passagem import Passagem
from view.passagem_tela import PassagemTela

class PassagemControlador:
    def __init__(self, sistema_controlador):
        self.__passagens = []
        self.__sistema_controlador = sistema_controlador
        self.__tela = PassagemTela()

    def incluir_passagem(self):
        #Coleta de Dados via outros Controladores
        # Selecionar Pessoa
        self.__sistema_controlador.pessoa_controlador.listar_pessoas()
        cpf_pessoa = self.__tela.seleciona_pessoa_por_cpf()
        pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(cpf_pessoa)
        if not pessoa:
            self.__tela.mostra_mensagem("Erro: Pessoa não encontrada.")
            return

        # Selecionar Transporte
        self.__sistema_controlador.transporte_controlador.listar_transportes()
        id_transporte = self.__tela.seleciona_transporte_por_id()
        transporte = self.__sistema_controlador.transporte_controlador._busca_transporte_por_id(id_transporte)
        if not transporte:
            self.__tela.mostra_mensagem("Erro: Transporte não encontrado.")
            return

        # Selecionar Cidades de Origem e Destino
        self.__sistema_controlador.cidade_controlador.listar_cidades()
        nome_origem = self.__tela.seleciona_cidade("origem")
        cidade_origem = self.__sistema_controlador.cidade_controlador._busca_cidade_por_nome(nome_origem)
        
        nome_destino = self.__tela.seleciona_cidade("destino")
        cidade_destino = self.__sistema_controlador.cidade_controlador._busca_cidade_por_nome(nome_destino)

        if not cidade_origem or not cidade_destino:
            self.__tela.mostra_mensagem("Erro: Cidade de origem ou destino não encontrada.")
            return
        
        if cidade_origem == cidade_destino:
            self.__tela.mostra_mensagem("Erro: A cidade de origem não pode ser a mesma que a de destino.")
            return
            
        # Pegar o Valor
        try:
            valor = self.__tela.pega_valor_passagem()
        except ValueError:
            self.__tela.mostra_mensagem("Erro: Valor inválido.")
            return

        # --- Criação do Objeto Passagem ---
        nova_passagem = Passagem(pessoa, valor, transporte, cidade_origem, cidade_destino)
        self.__passagens.append(nova_passagem)
        self.__tela.mostra_mensagem("Passagem emitida com sucesso!")

        return nova_passagem

    def alterar_passagem(self):
        self.listar_passagens()
        if not self.__passagens:
            return

        try:
            id_passagem = self.__tela.seleciona_passagem_por_id()
            passagem_a_alterar = self.__passagens[id_passagem]
        except (ValueError, IndexError):
            self.__tela.mostra_mensagem("Erro: ID de passagem inválido.")
            return

        dados_atuais = {
            "cpf": passagem_a_alterar.pessoa.cpf,
            "id_transporte": id(passagem_a_alterar.transportes),
            "origem": passagem_a_alterar.cidade_origem.nome,
            "destino": passagem_a_alterar.cidade_destino.nome,
            "valor": passagem_a_alterar.valor
        }

        novos_dados = self.__tela.pega_dados_para_alterar(dados_atuais)

        # Validação e atualização dos dados
        # Atualiza Pessoa
        pessoa = self.__sistema_controlador.pessoa_controlador._busca_pessoa_por_cpf(novos_dados["cpf"])
        if not pessoa:
            self.__tela.mostra_mensagem("Erro: Novo CPF não corresponde a uma pessoa cadastrada.")
            return
        passagem_a_alterar.pessoa = pessoa

        # Atualiza Transporte
        transporte = self.__sistema_controlador.transporte_controlador._busca_transporte_por_id(novos_dados["id_transporte"])
        if not transporte:
            self.__tela.mostra_mensagem("Erro: Novo ID de transporte não encontrado.")
            return
        passagem_a_alterar.transportes = transporte

        # Atualiza Cidades
        cidade_origem = self.__sistema_controlador.cidade_controlador._busca_cidade_por_nome(novos_dados["origem"])
        cidade_destino = self.__sistema_controlador.cidade_controlador._busca_cidade_por_nome(novos_dados["destino"])
        if not cidade_origem or not cidade_destino:
            self.__tela.mostra_mensagem("Erro: Nova cidade de origem ou destino não encontrada.")
            return
        passagem_a_alterar.cidade_origem = cidade_origem
        passagem_a_alterar.cidade_destino = cidade_destino

        # Atualiza Valor
        passagem_a_alterar.valor = novos_dados["valor"]

        self.__tela.mostra_mensagem("Passagem alterada com sucesso!")
        self.listar_passagens() 

    def listar_passagens(self):
        """Lista todas as passagens emitidas."""
        if not self.__passagens:
            self.__tela.mostra_mensagem("Nenhuma passagem foi emitida ainda.")
            return

        self.__tela.mostra_mensagem("\n--- LISTA DE PASSAGENS EMITIDAS ---")
        for i, passagem in enumerate(self.__passagens):
            dados = {
                "id": i,
                "passageiro": passagem.pessoa.nome,
                "cpf": passagem.pessoa.cpf,
                "origem": passagem.cidade_origem.nome,
                "destino": passagem.cidade_destino.nome,
                "transporte": f"{passagem.transportes.empresa.nome} - {passagem.transportes.meio_locomocao}",
                "valor": passagem.valor
            }
            self.__tela.mostra_passagem(dados)
        print("------------------------------------")


    def excluir_passagem(self):
        self.listar_passagens()
        if not self.__passagens:
            return

        try:
            id_passagem = self.__tela.seleciona_passagem_por_id()
            if 0 <= id_passagem < len(self.__passagens):
                passagem_removida = self.__passagens.pop(id_passagem)
                self.__tela.mostra_mensagem(f"Passagem de {passagem_removida.pessoa.nome} cancelada.")
            else:
                raise IndexError
        except (ValueError, IndexError):
            self.__tela.mostra_mensagem("Erro: ID de passagem inválido.")
            
    def retornar(self):
        self.__sistema_controlador.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_passagem,
            2: self.alterar_passagem,
            3: self.listar_passagens,
            4: self.excluir_passagem,
            0: self.retornar
        }
        while True:
            try:
                opcao = self.__tela.mostra_opcoes()
                lista_opcoes[opcao]()
            except (KeyError, ValueError):
                self.__tela.mostra_mensagem("Opção inválida, digite um número da lista.")