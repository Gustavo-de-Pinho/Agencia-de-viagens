class PasseioTuristicoTela:
    def mostra_opcoes(self) -> int:
        print("\n===== PASSEIOS TURÍSTICOS =====")
        print("> (1) Incluir Passeio")
        print("> (2) Alterar Passeio")
        print("> (3) Listar Passeios")
        print("> (4) Excluir Passeio")
        print("--------------------------------")
        print("> (0) Retornar")
        print("================================")
        print()
        
        try:
            return int(input("Escolha uma opção: "))
        except:
            return None

    def mostra_mensagem(self, msg: str):
        print(msg)

    def pega_dados_passeio(self) -> dict:
        print("\n-- DADOS DO PASSEIO --")
        nome = input("Nome: ")
        preco = input("Preço (ex: 49.90): ")
        return {"nome": nome, "preco": preco}

    def mostra_passeio(self, dados: dict):
        print(f"  > ID: {dados['id']} | Nome: {dados['nome']} | Preço: R$ {dados['preco']:.2f}")
    
    def seleciona_passeio_por_nome(self) -> str:
        return input("Informe o nome do passeio que deseja selecionar: ")

    def seleciona_passeio_por_id(self) -> int:
        return int(input("Informe o ID do passeio que deseja selecionar: "))