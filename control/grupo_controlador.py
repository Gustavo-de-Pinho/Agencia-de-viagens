from model.grupo import Grupo
from view.grupo_tela import GrupoTela
from model.pessoa import Pessoa

class GrupoControlador:
    def __init__(self, sistema_controlador):
        self.__membros = []
        self.__tela = GrupoTela()
        self.__sistema_controlador = sistema_controlador

    def incluir_membro(self):
        dados = self.__tela.incluir_membro()

        if dados is not None:
            membro_existe = False

            #Checa se membro com esse CPF já existe no grupo
            for membro in self.__membros: 
                if membro.cpf == dados["cpf"]:
                    membro_existe = True
                
            #Se membro não existe no grupo, adiciona ele
            if not membro_existe:
                self.__membros.append(
                    Pessoa(dados["nome"], dados["data_nascimento"], dados["cpf"], dados["telefone"]))
                
        else:
            self.__tela.mostrar_mensagem("Dados inválidos!")

    def remover_membro(self):
        cpf_membro = self.__tela.remover_membro()
        
        if cpf_membro is not None:
            for membro in self.__membros:
                if membro.cpf == cpf_membro:
                    self.__membros.remove(membro)
        else:
            self.__tela.mostrar_mensagem("Dados inválidos!")
    
    def alterar_membro(self):
        dados = self.__tela.editar_info_membro()

        if dados is not None:
            for membro in self.__membros:
                if membro.cpf == dados["cpf"]:
                    membro.nome = dados["nome"]
                    membro.data_nascimento = dados["data_nascimento"]
                    membro.telefone = dados["telefone"]
        else:
            self.__tela.mostrar_mensagem("Dados inválidos!")

    def listar_membros(self):

        for membro in self.__membros:
            self.__tela.mostrar_membro(membro)

    def retonar(self):
        self.__sistema_controlador.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.incluir_membro, 
            2: self.remover_membro, 
            3: self.alterar_membro, 
            4: self.listar_membros, 
            5: self.retonar}
        
        continua = True
        
        while continua:
            opcao = self.__tela.mostra_opcoes()

            if opcao is not None and opcao in opcoes.keys:
                if opcao == 5: #para de mostrar a tela de grupos se a opção escolhida for Retornar
                    continua = False
                opcoes[opcao]()
            else:
                self.__tela.mostrar_mensagem("Opção inválida!")
