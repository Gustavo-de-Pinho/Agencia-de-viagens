from model.empresa import Empresa
from model.transporte import Transporte
from view.transporte_tela import TransporteTela
from DAOs.empresa_dao import EmpresaDAO
from DAOs.transporte_dao import TransporteDAO

class TransporteControlador:
    def __init__(self, controlador_sistema):
        #self.__empresas = []
        self.__empresa_DAO = EmpresaDAO()               
        #self.__transportes = []
        self.__transporte_DAO = TransporteDAO()              
        self.__controlador_sistema = controlador_sistema
        self.__tela = TransporteTela()

    def busca_empresa_por_cnpj(self, cnpj: str) -> Empresa | None:
        return self.__empresa_DAO.get(cnpj)
    
    def busca_transporte_por_id(self, id: int) -> Transporte | None:
        return self.__transporte_DAO.get(id)
    
    # ---------- EMPRESA ----------
    def incluir_empresa(self):
        dados = self.__tela.pega_dados_empresa()
        if self.busca_empresa_por_cnpj(dados["cnpj"]):
            self.__tela.mostra_mensagem("Empresa já cadastrada!")
            return
        empresa = Empresa(dados["nome"], dados["cnpj"])
        self.__empresa_DAO.add(empresa)
        self.__tela.mostra_mensagem("Empresa cadastrada com sucesso.")

    def listar_empresas(self):
        empresas = self.__empresa_DAO.get_all()
        if not empresas:
            self.__tela.mostra_mensagem("Nenhuma empresa cadastrado.")
            return

        self.__tela.mostra_lista_empresas(empresas)

    def alterar_empresa(self):
        self.listar_empresas()
        cnpj = self.__tela.seleciona_empresa()
        emp = self.busca_empresa_por_cnpj(cnpj)
        if not emp:
            self.__tela.mostra_mensagem("Empresa não encontrada.")
            return
        novos_dados = self.__tela.pega_dados_empresa()
        emp.nome = novos_dados["nome"]
        emp.cnpj = novos_dados["cnpj"]
        self.__tela.mostra_mensagem("Empresa alterada.")

    def excluir_empresa(self):
        self.listar_empresas()
        cnpj = self.__tela.seleciona_empresa()
        emp = self.busca_empresa_por_cnpj(cnpj)
        if not emp:
            self.__tela.mostra_mensagem("Empresa não encontrada.")
            return
        
        lista_transportes = self.__transporte_DAO.get_all()
        for t in lista_transportes:
            if t.empresa.cnpj == emp.cnpj:
                self.__transporte_DAO.remove(t.id)
                
        self.__empresa_DAO.remove(emp.cnpj)
        self.__tela.mostra_mensagem("Empresa e seus transportes removidos.")

    # ---------- TRANSPORTE ----------
    def incluir_transporte(self):
        if not self.__empresa_DAO:
            self.__tela.mostra_mensagem("Cadastre pelo menos uma empresa primeiro.")
            return
        
        self.listar_empresas()
        cnpj = self.__tela.seleciona_empresa()
        empresa = self.busca_empresa_por_cnpj(cnpj)
        if not empresa:
            self.__tela.mostra_mensagem("Empresa inválida.")
            return
        
        meio = self.__tela.pega_meio_locomocao()
        
        transp = Transporte(empresa, 0, meio)
        
        self.__transporte_DAO.add(transp)
        self.__tela.mostra_mensagem("Transporte cadastrado.")

    def listar_transportes(self):
        transportes = self.__transporte_DAO.get_all()
        if not transportes:
            self.__tela.mostra_mensagem("Nenhum transporte cadastrado.")
            return

        self.__tela.mostra_lista_transporte(transportes)

    def alterar_transporte(self):
        self.listar_transportes()
        if not self.__transporte_DAO: return

        id_transporte = self.__tela.seleciona_transporte() 
        transp = self.busca_transporte_por_id(id_transporte)
        
        if not transp:
            self.__tela.mostra_mensagem("Transporte não encontrado.")
            return
        
        novo_meio = self.__tela.pega_meio_locomocao()
        transp.meio_locomocao = novo_meio
        
        self.__transporte_DAO.update(transp)
        self.__tela.mostra_mensagem("Transporte alterado.")

    def excluir_transporte(self):
        self.listar_transportes()
        if not self.__transporte_DAO: return

        id_transporte = self.__tela.seleciona_transporte()
        transp = self.busca_transporte_por_id(id_transporte)
        
        if not transp:
            self.__tela.mostra_mensagem("Transporte não encontrado.")
            return
            
        self.__transporte_DAO.remove(transp.id)
        self.__tela.mostra_mensagem("Transporte removido.")

    # ---------- NAVEGAÇÃO ----------

    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_empresa,
            2: self.alterar_empresa,
            3: self.listar_empresas,
            4: self.excluir_empresa,
            5: self.incluir_transporte,
            6: self.alterar_transporte,
            7: self.listar_transportes,
            8: self.excluir_transporte,
        }
        while True:
                opcao = self.__tela.mostra_opcoes()
                if opcao in lista_opcoes:
                    lista_opcoes[opcao]()
                elif opcao == 0:
                    break
                else:
                    self.__tela.mostra_mensagem("OPÇÃO INVÁLIDA")
