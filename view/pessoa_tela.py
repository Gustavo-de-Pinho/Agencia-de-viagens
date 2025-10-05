from datetime import datetime

class PessoaTela:
    def mostra_opcoes(self):
        print("======= OPÇÕES =======")
        print("> (1) Adicionar Pessoa no Sistema")
        print("> (2) Remover Pessoa do Sistema")
        print("> (3) Editar Informações de Pessoa")
        print("> (4) Listar pessoas no Sistema")
        print("> (5) Retonar")
        print("======================")

        opcao = input("Escolha uma opção: ")

        try:
            opcao = int(opcao)
            return opcao
        except:
            return None
        
    def pega_info_pessoa(self):
        nome = input("> Nome: ")
        data_nascimento = input("> Data de nascimento (DD-MM-AAAA): ")
        cpf = input("> CPF: ")
        telefone = input("> Telefone: ")

        if isinstance(nome, str) and isinstance(data_nascimento, datetime) and isinstance(cpf, str) and isinstance(telefone, str):
            return {
                "nome": nome,
                "data_nascimento": data_nascimento,
                "cpf": cpf,
                "telefone": telefone}
        else:
            return None
        
    def pega_cpf_pessoa(self):
        cpf = input("> CPF: ")

        if isinstance(cpf, str):
            return cpf
        else:
            return None

    def inclui_pessoa(self):
        print("======= ADICIONAR PESSOA NO SISTEMA =======")
        dados = self.pega_info_pessoa()
        print("===========================================")

        return dados
        
    def remove_pessoa(self):
        print("======= REMOVER PESSOA DO SISTEMA =======")
        cpf = self.pega_cpf_pessoa()
        print("=========================================")

        return cpf
        
    def edita_info_pessoa(self):
        print("======= EDITAR INFORMAÇÕES =======")
        cpf = self.pega_cpf_pessoa()
        print("==================================")
        novo_nome = input("> Novo Nome: ")
        nova_data_nascimento = input("> Nova Data de Nascimento: ")
        novo_telefone = input("> Novo Telefone: ")

        if cpf is not None and isinstance(novo_nome, str) and isinstance(nova_data_nascimento, datetime) and isinstance(novo_telefone, str):
            return {
                "nome": novo_nome,
                "data_nascimento": nova_data_nascimento,
                "cpf": cpf,
                "telefone": novo_telefone
            }
        else:
            return None

    def mostrar_pessoa(self, pessoa):
        print("=======================")
        print(f"> Nome: {pessoa.nome}")
        print(f"> Data de Nascimento: {pessoa.data_nascimento}")
        print(f"> CPF: {pessoa.cpf}")
        print(f"> Telefone: {pessoa.telefone}")
        print("=======================")

    def mostra_mensagem(self, msg):
        print(msg)