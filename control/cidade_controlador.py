from model.pais import Pais
from model.cidade import Cidade
from view.cidade_tela import CidadeTela
from DAOs.pais_dao import PaisDAO
from DAOs.cidade_dao import CidadeDAO

#Teste de branch
class CidadeControlador:
    def __init__(self, controlador_sistema):
        #self.__paises = []
        self.__pais_DAO = PaisDAO()
        #self.__cidades = []
        self.__cidade_DAO = CidadeDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela = CidadeTela()

    def busca_pais_por_id(self, id: int) -> Pais | None:
        return self.__pais_DAO.get(id)

    def busca_cidade_por_id(self, id: int) -> Cidade | None:
        return self.__cidade_DAO.get(id)

    def busca_pais_por_nome(self, nome: str) -> Pais | None:
        for p in self.__pais_DAO.get_all():
            if p.nome.lower() == nome.lower():
                return p
        return None

    def busca_cidade_por_nome(self, nome: str) -> Cidade | None:
        for c in self.__cidade_DAO.get_all():
            if c.nome.lower() == nome.lower():
                return c
        return None

    # ---------- PAÍS ----------
    def incluir_pais(self):
        nome_pais = self.__tela.pega_dados_pais()
        if self.busca_pais_por_nome(nome_pais):
            self.__tela.mostra_mensagem("Erro: País já cadastrado!")
            return
        
        pais = Pais(nome_pais)
        self.__pais_DAO.add(pais)
        self.__tela.mostra_mensagem("País cadastrado com sucesso.")

    def listar_paises(self):
        paises = self.__pais_DAO.get_all()
        if not paises:
            self.__tela.mostra_mensagem("Nenhum país cadastrado.")
            return

        self.__tela.mostra_lista_paises(paises)


    def alterar_pais(self):
        self.listar_paises()
        if not self.__pais_DAO: return

        id_pais = self.__tela.seleciona_pais_id() 
        pais = self.busca_pais_por_id(id_pais)

        if not pais:
            self.__tela.mostra_mensagem("País não encontrado.")
            return
            
        nome_novo = self.__tela.pega_dados_pais()
        pais.nome = nome_novo
        self.__pais_DAO.update(pais)
        self.__tela.mostra_mensagem("País alterado com sucesso.")

    def excluir_pais(self):
        self.listar_paises()
        if not self.__pais_DAO: return
        
        id_pais = self.__tela.seleciona_pais_id()
        pais = self.busca_pais_por_id(id_pais)

        if not pais:
            self.__tela.mostra_mensagem("País não encontrado.")
            return
        
        # Remove as cidades associadas a este país da lista geral de cidades
        for cidade in pais.cidades:
            self.__cidade_DAO.remove(cidade.id)

        
        self.__pais_DAO.remove(pais.id)
        self.__tela.mostra_mensagem("País e suas cidades foram removidos.")

    # ---------- CIDADE ----------
    def incluir_cidade(self):
        #Cadastra uma nova cidade e a associa a um país.
        if not self.__pais_DAO:
            self.__tela.mostra_mensagem("Erro: Cadastre um país antes de adicionar uma cidade.")
            return
        
        self.listar_paises()
        id_pais = self.__tela.seleciona_pais_id()
        pais = self.busca_pais_por_id(id_pais)

        if not pais:
            self.__tela.mostra_mensagem("País inválido.")
            return
        
        nome_cidade = self.__tela.pega_dados_cidade()
        if self.busca_cidade_por_nome(nome_cidade):
            self.__tela.mostra_mensagem("Erro: Já existe uma cidade com este nome.")
            return

        cidade = Cidade(nome_cidade)
        self.__cidade_DAO.add(cidade)
        pais.adicionar_cidade(cidade) # Adiciona a cidade na lista do país
        self.__pais_DAO.update(pais)
        self.__tela.mostra_mensagem(f"Cidade '{cidade.nome}' cadastrada em {pais.nome}.")

    def listar_cidades(self):
        cidades = self.__cidade_DAO.get_all()
        if not cidades:
            self.__tela.mostra_mensagem("Nenhuma cidade cadastrada.")
            return

        self.__tela.mostra_lista_cidades(cidades)

    def alterar_cidade(self):
        self.listar_cidades()
        if not self.__cidade_DAO: return

        id_cidade_antigo = self.__tela.seleciona_cidade_id()
        cidade = self.busca_cidade_por_id(id_cidade_antigo)

        if not cidade:
            self.__tela.mostra_mensagem("Cidade não encontrada.")
            return
            
        nome_novo = self.__tela.pega_dados_cidade()
        cidade.nome = nome_novo
        self.__tela.mostra_mensagem("Cidade alterada com sucesso.")

    def excluir_cidade(self):
        self.listar_cidades()
        if not self.__cidade_DAO: return

        id_cidade = self.__tela.seleciona_cidade_id()
        cidade = self.busca_cidade_por_id(id_cidade)

        if not cidade:
            self.__tela.mostra_mensagem("Cidade não encontrada.")
            return
        
        for pais in self.__pais_DAO.get_all():
            if cidade in pais.cidades:
                pais.cidades.remove(cidade)
                self.__pais_DAO.update(pais)
                break
        
        self.__cidade_DAO.remove(cidade.id)
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
        return self.__pais_DAO.get_all()
    
    @property
    def cidades(self):
        return self.__cidade_DAO.get_all()