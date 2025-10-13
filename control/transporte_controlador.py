from model.empresa import Empresa
from model.transporte import Transporte
from view.transporte_tela import TransporteTela


class TransporteControlador:
    def __init__(self, controlador_sistema):
        self.__empresas = []               
        self.__transportes = []            
        self.__controlador_sistema = controlador_sistema
        self.__tela = TransporteTela()

    def _busca_empresa_por_cnpj(self, cnpj: str) -> Empresa | None:
        for e in self.__empresas:
            if e.cnpj == cnpj:
                return e
        return None

    '''def _busca_transporte_por_id(self, id_transp: int) -> Transporte | None:
        for t in self.__transportes:
            if id(t) == id_transp:
                return t
        return None'''
    
    def busca_transporte_por_id(self, indice: int) -> Transporte | None:
        try:
            if 0 <= indice < len(self.__transportes):
                return self.__transportes[indice]
            return None 
        except TypeError:
            return None

    # ---------- EMPRESA ----------
    def incluir_empresa(self):
        dados = self.__tela.pega_dados_empresa()
        if self._busca_empresa_por_cnpj(dados["cnpj"]):
            self.__tela.mostra_mensagem("Empresa já cadastrada!")
            return
        empresa = Empresa(dados["nome"], dados["cnpj"])
        self.__empresas.append(empresa)
        self.__tela.mostra_mensagem("Empresa cadastrada com sucesso.")

    def listar_empresas(self):
        if not self.__empresas:
            self.__tela.mostra_mensagem("Nenhuma empresa cadastrada.")
            return
        for e in self.__empresas:
            self.__tela.mostra_empresa({"nome": e.nome, "cnpj": e.cnpj})

    def alterar_empresa(self):
        self.listar_empresas()
        cnpj = self.__tela.seleciona_empresa()
        emp = self._busca_empresa_por_cnpj(cnpj)
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
        emp = self._busca_empresa_por_cnpj(cnpj)
        if not emp:
            self.__tela.mostra_mensagem("Empresa não encontrada.")
            return
        
        self.__transportes = [t for t in self.__transportes if t.empresa != emp]
        self.__empresas.remove(emp)
        self.__tela.mostra_mensagem("Empresa e seus transportes removidos.")

    # ---------- TRANSPORTE ----------
    def incluir_transporte(self):
        if not self.__empresas:
            self.__tela.mostra_mensagem("Cadastre pelo menos uma empresa primeiro.")
            return
        
        self.listar_empresas()
        cnpj = self.__tela.seleciona_empresa()
        empresa = self._busca_empresa_por_cnpj(cnpj)
        if not empresa:
            self.__tela.mostra_mensagem("Empresa inválida.")
            return
        
        meio = self.__tela.pega_meio_locomocao()
        transp = Transporte(empresa, meio)
        self.__transportes.append(transp)
        self.__tela.mostra_mensagem("Transporte cadastrado.")

    def listar_transportes(self):
        if not self.__transportes:
            self.__tela.mostra_mensagem("Nenhum transporte cadastrado.")
            return
        for idx, t in enumerate(self.__transportes):
            self.__tela.mostra_transporte(idx, {
                "empresa": t.empresa.nome,
                "cnpj": t.empresa.cnpj,
                "meio": t.meio_locomocao
            })

    def alterar_transporte(self):
        self.listar_transportes()
        idx = self.__tela.seleciona_transporte() 
        try:
            transp = self.__transportes[idx]
        except IndexError:
            self.__tela.mostra_mensagem("Transporte inválido.")
            return
        
        novo_meio = self.__tela.pega_meio_locomocao()
        transp.meio_locomocao = novo_meio
        self.__tela.mostra_mensagem("Transporte alterado.")

    def excluir_transporte(self):
        self.listar_transportes()
        idx = self.__tela.seleciona_transporte()
        try:
            transp = self.__transportes[idx]
        except IndexError:
            self.__tela.mostra_mensagem("Transporte inválido.")
            return
        self.__transportes.remove(transp)
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
