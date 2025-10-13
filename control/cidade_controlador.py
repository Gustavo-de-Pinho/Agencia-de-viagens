from model.pais import Pais
from model.cidade import Cidade
from view.cidade_tela import CidadeTela

class CidadeControlador:
    def __init__(self, controlador_sistema):
        self.__paises = []
        self.__cidades = []
        self.__controlador_sistema = controlador_sistema
        self.__tela = CidadeTela()

    def _busca_pais_por_nome(self, nome: str) -> Pais | None:
        for p in self.__paises:
            if p.nome.lower() == nome.lower():
                return p
        return None

    def _busca_cidade_por_nome(self, nome: str) -> Cidade | None:
        for c in self.__cidades:
            if c.nome.lower() == nome.lower():
                return c
        return None

    # ---------- PAÍS ----------
    def incluir_pais(self):
        nome_pais = self.__tela.pega_dados_pais()
        if self._busca_pais_por_nome(nome_pais):
            self.__tela.mostra_mensagem("Erro: País já cadastrado!")
            return
        
        pais = Pais(nome_pais)
        self.__paises.append(pais)
        self.__tela.mostra_mensagem("País cadastrado com sucesso.")

    def listar_paises(self):
        if not self.__paises:
            self.__tela.mostra_mensagem("Nenhum país cadastrado.")
            return
            
        self.__tela.mostra_mensagem("\n--- LISTA DE PAÍSES ---")
        for p in self.__paises:
            self.__tela.mostra_pais({"nome": p.nome})
        print("-----------------------")


    def alterar_pais(self):
        self.listar_paises()
        if not self.__paises: return

        nome_antigo = self.__tela.seleciona_pais()
        pais = self._busca_pais_por_nome(nome_antigo)

        if not pais:
            self.__tela.mostra_mensagem("País não encontrado.")
            return
            
        nome_novo = self.__tela.pega_dados_pais()
        pais.nome = nome_novo
        self.__tela.mostra_mensagem("País alterado com sucesso.")

    def excluir_pais(self):
        self.listar_paises()
        if not self.__paises: return
        
        nome_pais = self.__tela.seleciona_pais()
        pais = self._busca_pais_por_nome(nome_pais)

        if not pais:
            self.__tela.mostra_mensagem("País não encontrado.")
            return
        
        # Remove as cidades associadas a este país da lista geral de cidades
        self.__cidades = [c for c in self.__cidades if c not in pais.cidades]
        
        self.__paises.remove(pais)
        self.__tela.mostra_mensagem("País e suas cidades foram removidos.")

    # ---------- CIDADE ----------
    def incluir_cidade(self):
        #Cadastra uma nova cidade e a associa a um país.
        if not self.__paises:
            self.__tela.mostra_mensagem("Erro: Cadastre um país antes de adicionar uma cidade.")
            return
        
        self.listar_paises()
        nome_pais = self.__tela.seleciona_pais()
        pais = self._busca_pais_por_nome(nome_pais)

        if not pais:
            self.__tela.mostra_mensagem("País inválido.")
            return
        
        nome_cidade = self.__tela.pega_dados_cidade()
        if self._busca_cidade_por_nome(nome_cidade):
            self.__tela.mostra_mensagem("Erro: Já existe uma cidade com este nome.")
            return

        cidade = Cidade(nome_cidade)
        self.__cidades.append(cidade)
        pais.adicionar_cidade(cidade) # Adiciona a cidade na lista do país
        self.__tela.mostra_mensagem(f"Cidade '{cidade.nome}' cadastrada em {pais.nome}.")

    def listar_cidades(self):
        if not self.__cidades:
            self.__tela.mostra_mensagem("Nenhuma cidade cadastrada.")
            return
        
        self.__tela.mostra_mensagem("\n--- LISTA DE CIDADES ---")
        for pais in self.__paises:
            if pais.cidades:
                for cidade in pais.cidades:
                    self.__tela.mostra_cidade({
                        "nome_cidade": cidade.nome,
                        "nome_pais": pais.nome
                    })
        print("------------------------")

    def alterar_cidade(self):
        self.listar_cidades()
        if not self.__cidades: return

        nome_antigo = self.__tela.seleciona_cidade()
        cidade = self._busca_cidade_por_nome(nome_antigo)

        if not cidade:
            self.__tela.mostra_mensagem("Cidade não encontrada.")
            return
            
        nome_novo = self.__tela.pega_dados_cidade()
        cidade.nome = nome_novo
        self.__tela.mostra_mensagem("Cidade alterada com sucesso.")

    def excluir_cidade(self):
        self.listar_cidades()
        if not self.__cidades: return

        nome_cidade = self.__tela.seleciona_cidade()
        cidade = self._busca_cidade_por_nome(nome_cidade)

        if not cidade:
            self.__tela.mostra_mensagem("Cidade não encontrada.")
            return
        
        for pais in self.__paises:
            if cidade in pais.cidades:
                pais.cidades.remove(cidade)
                break
        
        self.__cidades.remove(cidade)
        self.__tela.mostra_mensagem("Cidade removida com sucesso.")

    # ---------- NAVEGAÇÃO ----------

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_pais,
            2: self.alterar_pais,
            3: self.listar_paises,
            4: self.excluir_pais,
            5: self.incluir_cidade,
            6: self.alterar_cidade,
            7: self.listar_cidades,
            8: self.excluir_cidade,
        }
        while True:
            try:
                opcao = self.__tela.mostra_opcoes()

                if opcao in lista_opcoes:
                    lista_opcoes[opcao]()
                elif opcao == 0:
                    break
                else:
                    self.__tela.mostra_mensagem("OPÇÃO INVÁLIDA")
            except (KeyError, ValueError):
                self.__tela.mostra_mensagem("Opção inválida, digite um número da lista.")
    
    @property
    def paises(self):
        return self.__paises
    
    @property
    def cidades(self):
        return self.__cidades