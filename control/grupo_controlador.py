from model.grupo import Grupo
from view.grupo_tela import GrupoTela
from DAOs.grupo_dao import GrupoDAO


class GrupoControlador:
    def __init__(self, sistema_controlador):

        self.__grupo_DAO = GrupoDAO()
        self.__tela = GrupoTela()
        self.__sistema_controlador = sistema_controlador

    def grupo_por_codigo(self, codigo):
        return self.__grupo_DAO.get(codigo)
    
    def pessoa_em_grupo(self, pessoa, grupo):
        try:
            if pessoa in grupo.membros:
                return True
            else:
                return False
        except:
            return False

    def criar_grupo(self):
        self.listar_grupos()
        
        codigo = self.__tela.criar_grupo()
        grupo_existe = False
        
        for grupo in self.__grupo_DAO.get_all():
            if grupo.codigo == codigo:
                grupo_existe = True

        if not grupo_existe and isinstance(codigo, int):
            novo_grupo = Grupo(codigo)
            self.__grupo_DAO.add(novo_grupo)
        else:
            self.__tela.mostrar_mensagem("GRUPO JA EXISTE OU CÓDIGO NÃO NUMÉRICO!")

    def excluir_grupo(self):
        self.listar_grupos()

        codigo = self.__tela.excluir_grupo()
        codigo_existe = False

        grupo = self.__grupo_DAO.get(codigo)
        

        if grupo is not None and grupo in self.__grupo_DAO.get_all():
                    codigo_existe = True
                    self.__grupo_DAO.remove(codigo)

        if codigo_existe:
            self.__tela.mostrar_mensagem("GRUPO REMOVIDO")
        else:
            self.__tela.mostrar_mensagem("GRUPO NÃO EXISTE!")

    def adicionar_membro(self):
        self.__sistema_controlador.pessoa_controlador.listar_pessoas()
        
        dados = self.__tela.adicionar_membro()

        if dados is not None:
            grupo = self.__grupo_DAO.get(dados["codigo"])

            if grupo is not None:
                pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(dados["cpf"])

                if pessoa is not None:
                    codigo = dados ["codigo"]
                    self.__grupo_DAO.get(codigo).membros.append(pessoa)

            self.__grupo_DAO.update(grupo)

    def remover_membro(self):
        self.listar_membros()

        dados = self.__tela.remover_membro()
        pessoa_existe = False
        grupo_existe = False
        membro_no_grupo = False

        if dados is not None:
            grupo = self.__grupo_DAO.get(dados["codigo"])

            if dados is not None and grupo in self.__grupo_DAO.get_all():
                pessoa = self.__sistema_controlador.pessoa_controlador.pessoa_por_cpf(dados["cpf"])
                if pessoa is not None:
                    for membro in self.__grupo_DAO.get(dados["codigo"]).membros:
                        if membro.cpf == pessoa.cpf:
                            membro_no_grupo = True
                            self.__grupo_DAO.get(dados["codigo"]).membros.remove(membro)

            self.__grupo_DAO.update(grupo)

        if not pessoa_existe and not grupo_existe and not membro_no_grupo:
            self.__tela.mostrar_mensagem("GRUPO OU PESSOA INEXISTENTE OU PESSOA NÃO ESTÁ NO GRUPO")
        else:
            self.__tela.mostrar_mensagem("MEMBRO REMOVIDO COM SUCESSO")

    def listar_membros(self):
        self.listar_grupos()
        
        codigo = self.__tela.listar_membros()
        grupo = self.__grupo_DAO.get(codigo)

        dados_membros = []

        if grupo is not None:
            for membro in grupo.membros:
                dados_membros.append({
                    "nome": membro.nome,
                    "cpf": membro.cpf,
                    "data_nascimento": membro.data_nascimento,
                    "telefone": membro.telefone
                })
            self.__tela.mostrar_membros(dados_membros)

    def listar_grupos(self):
        
        dados_grupos = []

        for grupo in self.__grupo_DAO.get_all():
            dados_grupos.append({"codigo": grupo.codigo})

        self.__tela.mostrar_grupos(dados_grupos)

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
        return self.__grupo_DAO.get_all()