class CidadeTela:
    def mostra_opcoes(self) -> int:
        print("===========================")
        print("---------- PAÍS -----------")
        print("> (1) Cadastrar País")
        print("> (2) Alterar País")
        print("> (3) Listar Países")
        print("> (4) Excluir País")
        print("---------- CIDADE ----------")
        print("> (5) Cadastrar Cidade")
        print("> (6) Alterar Cidade")
        print("> (7) Listar Cidades")
        print("> (8) Excluir Cidade")
        print("---------------------------")
        print("> (0) Retornar")
        print("===========================")
        print()
        
        return int(input("Escolha uma opção: "))
    
    def mostra_mensagem(self, msg: str):
        print(msg)

    # --- Métodos para País ---
    def pega_dados_pais(self) -> str:
        print("\n-- DADOS DO PAÍS --")
        return input("Nome: ")

    def mostra_pais(self, dados: dict):
        print(f"  > {dados['nome']}")

    def seleciona_pais(self) -> str:
        return input("Informe o nome do país: ")

    # --- Métodos para Cidade ---
    def pega_dados_cidade(self) -> str:
        print("\n-- DADOS DA CIDADE --")
        return input("Nome: ")

    def mostra_cidade(self, dados: dict):
        print(f"  > Cidade: {dados['nome_cidade']} | País: {dados['nome_pais']}")

    def seleciona_cidade(self) -> str:
        return input("Informe o nome da cidade: ")