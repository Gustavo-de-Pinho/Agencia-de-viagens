from model.pessoa import Pessoa
from view.pessoa_tela import PessoaTela
from DAOs.pessoa_dao import PessoaDAO


class PessoaControlador:
    def __init__(self, sistema_controlador):
        self.__pessoa_DAO = PessoaDAO()
        self.__tela = PessoaTela()
        self.__sistema_controlador = sistema_controlador

    def pessoa_por_cpf(self, cpf):
        for pessoa in self.__pessoa_DAO.get_all():
            if pessoa.cpf == cpf:
                return pessoa
        return None 

    def incluir_pessoa(self):
        dados = self.__tela.inclui_pessoa()
        cpf_existe = False

        if dados is not None:
            for pessoa in self.__pessoa_DAO.get_all():
                if pessoa.cpf == dados["cpf"]:
                    cpf_existe = True

            if not cpf_existe:
                pessoa = Pessoa(dados["nome"], 
                                dados["data_nascimento"], 
                                dados["cpf"], 
                                dados["telefone"])
                
                if pessoa.nome is not None and pessoa.data_nascimento is not None and pessoa.cpf is not None and pessoa.telefone is not None:
                    self.__pessoa_DAO.add(pessoa)
                    self.__tela.mostra_mensagem("PESSOA ADICIONADA")
                else:
                    self.__tela.mostra_mensagem("DADOS INVÁLIDOS OU PESSOA É MENOR DE IDADE")
            else:
                self.__tela.mostra_mensagem("CPF JÁ ESTÁ NO SISTEMA")
        else:
            self.__tela.mostra_mensagem("DADOS INVÁLIDOS")

    def remover_pessoa(self):
        cpf = self.__tela.remove_pessoa()

        if cpf is not None:
            self.__pessoa_DAO.remove(cpf)
        else:
            self.__tela.mostra_mensagem("DADOS INVÁLIDOS")

    def editar_info_pessoa(self):
        dados = self.__tela.edita_info_pessoa()
        pessoa_encontrada = False

        if dados is not None:
            for pessoa in self.__pessoa_DAO.get_all():
                if pessoa.cpf == dados["cpf"]:

                    pessoa.nome = dados["nome"]
                    pessoa.data_nascimento = dados["data_nascimento"]
                    pessoa.telefone = dados["telefone"]
                    pessoa_encontrada = True

                    self.__pessoa_DAO.update(pessoa)
            
            if pessoa_encontrada:
                self.__tela.mostra_mensagem("DADOS EDITADOS")
            else:
                self.__tela.mostra_mensagem("PESSOA NÃO ENCONTRADA NO SISTEMA")
        
        else:
            self.__tela.mostra_mensagem("DADOS INVÁLIDOS")

    def listar_pessoas(self):
        for pessoa in self.__pessoa_DAO.get_all():
            pessoa_dict = {
                "nome": pessoa.nome,
                "data_nascimento": pessoa.data_nascimento,
                "cpf": pessoa.cpf,
                "telefone": pessoa.telefone
            }
            self.__tela.mostrar_pessoa(pessoa_dict)

    def abre_tela(self):
        opcoes = {
            1: self.incluir_pessoa,
            2: self.remover_pessoa,
            3: self.editar_info_pessoa,
            4: self.listar_pessoas,
        }

        continua = True

        while continua:
            opcao = self.__tela.mostra_opcoes()

            if opcao is not None and opcao in opcoes:

                opcoes[opcao]()

            elif opcao == 0:
                break

            else:
                self.__tela.mostra_mensagem("OPÇÃO INVÁLIDA")

    @property
    def pessoas(self):
        return self.__pessoa_DAO.get_all
