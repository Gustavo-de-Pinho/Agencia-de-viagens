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
        print("> (9) GERAR RELATÓRIO")
        print("> (0) SAIR")
        print("=====================")
        print()
        
        opcao = input("Escolha uma opção: ")
        
        try:
            opcao = int(opcao)
            return opcao
        except:
            return None
        
    def gerar_relatorio(self, dados):
        print("======= RELATÓRIO =======")
        print(f"> Número de pessoas: {dados["pessoas"]}")
        print(f"> Número de grupos: {dados["grupos"]}")
        print(f"> Número de cidades: {dados["cidades"]}")
        print(f"> Número de países: {dados["paises"]}")
        print(f"> Número de passeios turísticos: {dados["passeios_turisticos"]}")
        print("=========================")

    def mostrar_mensagem(self, msg):
        print(msg)