class SistemaTela:
    def opcoes(self):
        print("====== OPÇÕES ======")
        print("> (1) PESSOA")
        print("> (2) GRUPO")
        print("> (3) PACOTE")
        print("> (4) PAGAMENTO")
        print("> (5) CIDADE/PAÍS")
        print("> (6) LOCAL")
        print("> (7) PASSEIO TURÍSTICO")
        print("> (8) TRANSPORTE")
        print("> (0) SAIR")
        print("=====================")
        print()
        
        opcao = input("Escolha uma opção: ")
        
        try:
            opcao = int(opcao)
            return opcao
        except:
            return None
        
    def mostrar_mensagem(self, msg):
        print(msg)