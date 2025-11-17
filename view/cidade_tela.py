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
        
        try:
            return int(input("Escolha uma opção: "))
        except:
            return None
    
    def mostra_mensagem(self, msg: str):
        print(msg)

    # --- Métodos para País ---
    def pega_dados_pais(self) -> str:
        print("\n-- DADOS DO PAÍS --")
        return input("Nome: ")

    def mostra_pais(self, dados: dict):
        print(f"  > ID: {dados['id']} - {dados['nome']}")

    def seleciona_pais_id(self) -> int:
        while True:
            try:
                id_pais = int(input("Informe o ID do país: "))
                return id_pais
            except ValueError:
                print("ERRO: O ID deve ser um número inteiro.")

    # --- Métodos para Cidade ---
    def pega_dados_cidade(self) -> str:
        print("\n-- DADOS DA CIDADE --")
        return input("Nome: ")

    def mostra_cidade(self, dados: dict):
        print(f"  > ID: {dados['id_cidade']} - Cidade: {dados['nome_cidade']} | País: {dados['nome_pais']}")

    def seleciona_cidade_id(self) -> int:
        while True:
            try:
                id_cidade = int(input("Informe o ID da cidade: "))
                return id_cidade
            except ValueError:
                print("ERRO: O ID deve ser um número inteiro.")