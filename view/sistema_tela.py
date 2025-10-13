class SistemaTela:
    def opcoes(self):
        print("====== OPÇÕES ======")
        print("> (1) PESSOA")
        print("> (2) GRUPO")
        print("> (3) CIDADE/PAÍS")
        print("> (4) PASSEIO TURÍSTICO")
        print("> (5) LOCAL")
        print("> (6) TRANSPORTE")
        print("> (7) PACOTE")
        print("> (8) PAGAMENTO")
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