class PasseioTuristicoTela:
    def mostra_opcoes(self) -> int:
        print("\n===== PASSEIOS TURÍSTICOS =====")
        print("> (1) Incluir Passeio")
        print("> (2) Alterar Passeio")
        print("> (3) Listar Passeios")
        print("> (4) Excluir Passeio")
        print("> (0) Retornar")
        
        while True:
            opcao = int(input("Escolha uma opção: "))
            return opcao

    def mostra_mensagem(self, msg: str):
        print(msg)

    def pega_dados_passeio(self) -> dict:
        print("\n-- DADOS DO PASSEIO --")
        nome = input("Nome: ")
        preco = input("Preço (ex: 49.90): ")
        return {"nome": nome, "preco": preco}

    def mostra_passeio(self, dados: dict):
        print(f"  > Nome: {dados['nome']} | Preço: R$ {dados['preco']:.2f}")

    def seleciona_passeio(self) -> str:
        return input("Informe o nome do passeio que deseja selecionar: ")