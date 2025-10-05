from datetime import datetime

class GrupoTela:
    def mostra_opcoes(self):
        print("====== OPÇÕES ======")
        print("> (1) Criar Grupo")
        print("> (2) Excluir Grupo")
        print("> (3) Incluir Membro")
        print("> (4) Remover Membro")
        print("> (5) Listar Membros do Grupo")
        print("> (6) Retonar")
        print("=====================")
        print()

        opcao = input("Escolha uma opção: ")

        #Tenta converter o input em inteiro. Se falhar retorna None
        try:
            opcao = int(opcao)
            return opcao
        except:
            return None
        
    def pegar_codigo_grupo(self):
        codigo = input("> Código do Grupo: ")

        try:
            codigo = int(codigo)
            return codigo
        except:
            return None        

    def criar_grupo(self):
        print("======= CRIAR GRUPO =======")
        codigo = self.pegar_codigo_grupo()
        print("===========================")

        return codigo
        
    def excluir_grupo(self):
        print("======= EXCLUIR GRUPO =======")
        codigo = self.pegar_codigo_grupo()
        print("=============================")

        return codigo

    def adicionar_membro(self):
        print("======= ADICIONAR MEMBRO =======")
        codigo = self.pegar_codigo_grupo()
        cpf = input("> CPF: ")
        print("================================")

        if isinstance(cpf, str) and codigo is not None:
                return {"codigo": codigo, "cpf": cpf}
        else:
            return None
        
    def remover_membro(self):
        print("======= REMOVER MEMBRO =======")
        codigo = self.pegar_codigo_grupo()
        cpf = input("> CPF: ")
        print("==============================")

        if isinstance(cpf, str) and codigo is not None:
            return {"codigo": codigo, "cpf": cpf}
        else:
            return None
        
    def listar_membros(self):
        print("======= LISTAR MEMBROS DO GRUPO =======")
        codigo = self.pegar_codigo_grupo()
        print("=======================================")

        if codigo is not None:
            return codigo
        else:
            return None

    def mostrar_mensagem(self, msg):
        print(msg)
