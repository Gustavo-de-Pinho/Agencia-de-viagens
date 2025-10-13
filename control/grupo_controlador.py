from model.grupo import Grupo
from view.grupo_tela import GrupoTela


class GrupoControlador:
    def __init__(self, sistema_controlador):
        self.__grupos = {}
        self.__tela = GrupoTela()
        self.__sistema_controlador = sistema_controlador

    def grupo_por_codigo(self, codigo):
        if codigo in self.__grupos:
            return self.__grupos[codigo]
        else:
            return None
    
    def pessoa_em_grupo(self, pessoa, grupo):
        try:
            if pessoa in grupo.membros:
                return True
            else:
                return False
        except:
            return False

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

        if dados is not None and dados["codigo"] in self.__grupos:
            pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(dados["cpf"])

            if pessoa is not None:
                codigo = dados ["codigo"]
                self.__grupos[codigo].membros.append(pessoa)

    def remover_membro(self):
        dados = self.__tela.remover_membro()
        pessoa_existe = False
        grupo_existe = False
        membro_no_grupo = False

        #MONSTRUOSIDADE!!!!!!!!!!
        if dados is not None and dados["codigo"] in self.__grupos:
            pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(dados["cpf"])
            if pessoa is not None:
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
        if codigo in self.__grupos:
            for membro in self.__grupos[codigo].membros:
                membro_dict = {
                    "nome": membro.nome,
                    "cpf": membro.cpf,
                    "data_nascimento": membro.data_nascimento,
                    "telefone": membro.telefone
                }
                self.__tela.mostrar_membros(membro_dict)

    def abre_tela(self):
        opcoes = {
            1: self.criar_grupo,
            2: self.excluir_grupo,
            3: self.adicionar_membro,
            4: self.remover_membro,
            5: self.listar_membros}
        
        continua = True

        while continua:
            opcao = self.__tela.mostra_opcoes()

            if opcao is not None and opcao in opcoes:
                opcoes[opcao]()

            elif opcao == 0:
                break

            else:
                self.__tela.mostrar_mensagem("OPÇÃO INVÁLIDA")

    @property
    def grupos(self):
        return self.__grupos