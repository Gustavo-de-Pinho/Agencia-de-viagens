from model.grupo import Grupo
from view.grupo_tela import GrupoTela


class GrupoControlador:
    def __init__(self, sistema_controlador):
        self.__grupos = {}
        self.__tela = GrupoTela()
        self.__sistema_controlador = sistema_controlador

    def criar_grupo(self):
        codigo = self.__tela.criar_grupo()
        codigo_existe = False

        if codigo is not None and codigo not in self.__grupos:
            self.__grupos[codigo] = Grupo(codigo)

            if not codigo_existe:
                self.__tela.mostrar_mensagem("GRUPO CRIADO")
            else:
                self.__tela.mostrar_mensagem("GRUPO JÁ EXISTE!")

        else:
            self.__tela.mostrar_mensagem("CÓDIGO INVÁLIDO. CÓDIGO DEVE SER NUMÉRICO")

    def excluir_grupo(self):
        codigo = self.__tela.excluir_grupo()
        codigo_existe = False

        if codigo is not None and codigo in self.__grupos:
                    codigo_existe = True
                    self.__grupos.pop(codigo)

        if codigo_existe:
            self.__tela.mostrar_mensagem("GRUPO REMOVIDO")
        else:
            self.__tela.mostrar_mensagem("GRUPO NÃO EXISTE!")

    def adicionar_membro(self):
        dados = self.__tela.adicionar_membro()
        pessoa_existe = False
        grupo_existe = False

        if dados is not None and dados["codigo"] in self.__grupos:
            grupo_existe = True
            for pessoa in self.__sistema_controlador.pessoa_controlador.pessoas:
                if pessoa.cpf == dados["cpf"]:
                    pessoa_existe = True
                    self.__grupos[dados["codigo"]].membros.append(pessoa)

        if not pessoa_existe and not grupo_existe:
            self.__tela.mostrar_mensagem("GRUPO OU PESSOA INEXISTENTE")
        else:
            self.__tela.mostrar_mensagem("PESSOA ADICIONADA COM SUCESSO")

    def remover_membro(self):
        dados = self.__tela.remover_membro()
        pessoa_existe = False
        grupo_existe = False
        membro_no_grupo = False

        #MONSTRUOSIDADE!!!!!!!!!!
        if dados is not None and dados["codigo"] in self.__grupos:
            grupo_existe = True
            for pessoa in self.__sistema_controlador.pessoa_controlador.pessoas:
                if pessoa.cpf == dados["cpf"]:
                    pessoa_existe = True
                    for membro in self.__grupos[dados["codigo"]].membros:
                        if membro.cpf == pessoa.cpf:
                            membro_no_grupo = True
                            self.__grupos[dados["codigo"]].membros.remove(membro)

        if not pessoa_existe and not grupo_existe and not membro_no_grupo:
            self.__tela.mostrar_mensagem("GRUPO OU PESSOA INEXISTENTE OU PESSOA NÃO ESTÁ NO GRUPO")
        else:
            self.__tela.mostrar_mensagem("MEMBRO REMOVIDO COM SUCESSO")

    def listar_membros(self):
        codigo = self.__tela.listar_membros()

        for membro in self.__grupos[codigo].membros:
            self.__sistema_controlador.pessoa_controlador.tela.mostrar_pessoa(membro)

    def retornar(self):
        self.__sistema_controlador.abre_tela()

    def abre_tela(self):
        opcoes = {
            1: self.criar_grupo,
            2: self.excluir_grupo,
            3: self.adicionar_membro,
            4: self.remover_membro,
            5: self.listar_membros,
            6: self.retornar}
        
        opcao = self.__tela.mostra_opcoes()
        continua = True

        while continua:
            if opcao is not None and opcao in opcoes:
                if opcao == 6:
                    continua = False
                    opcoes[opcao]()
                    break

                opcoes[opcao]()

                opcao = self.__tela.mostra_opcoes()

            else:
                self.__tela.mostrar_mensagem("OPÇÃO INVÁLIDA")
