from datetime import datetime

class GrupoTela:
    def mostra_opcoes(self):
        print("====== OPÇÕES ======")
        print("> (1) Incluir Membro")
        print("> (2) Remover Membro")
        print("> (3) Editar Informações de um Membro")
        print("> (4) Listar Membros do Grupo")
        print("> (5) Retonar")
        print("=====================")
        print()

        opcao = input("Escolha uma opção: ")

        #Tenta converter o input em inteiro. Se falhar retorna None
        try:
            opcao = int(opcao)
            return opcao
        except:
            return None

    def incluir_membro(self):
        print("======= INCLUIR MEMBRO =======")
        nome = input("> Nome: ")
        data_nascimento = input("> Data de nascimento (DD-MM-AAAA): ")
        cpf = input("> CPF: ")
        telefone = input("> Telefone: ")
        print()

        if isinstance(nome, str) and isinstance(data_nascimento, datetime) and isinstance(cpf, str) and isinstance(telefone, str):
            return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "telefone": telefone}
        else:
            return None
        
    def remover_membro(self):
        print("======= REMOVER MEMBRO =======")
        cpf = input("> CPF: ")

        return cpf
    
    def editar_info_membro(self):
        print("======= EDITAR MEMBRO =======")
        cpf = input("> CPF: ")
        print()
        print("Novas informações: ")
        nome = input("> Nome: ")
        data_nascimento = input("> Data de nascimento (DD-MM-AAAA): ")
        telefone = input("> Telefone: ")

        if isinstance(nome, str) and isinstance(data_nascimento, datetime) and isinstance(cpf, str) and isinstance(telefone, str):
            return {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "telefone": telefone}
        else:
            return None
        
    def mostrar_membro(self, membro):
        print(f"> Nome: {membro.nome}")
        print(f"> Data de Nascimento: {membro.data_nascimento}")
        print(f"> CPF: {membro.cpf}")
        print(f"> Telefone: {membro.telefone}")
        print()

    def mostrar_mensagem(msg):
        print(msg)