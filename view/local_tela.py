class LocalTela:
    def mostra_opcoes(self) -> int:
        print("=========== LOCAIS ===========")
        print("> (1) Cadastrar Local (associar a uma cidade)")
        print("> (2) Listar Locais")
        print("> (3) Adicionar Passeio a um Local")
        print("> (4) Excluir Local")
        print("----------------------------")
        print("> (0) Retornar")
        print("===============================")
        print()
        
        try:
            return int(input("Escolha uma opção: "))
        except:
            return None
    
    def mostra_mensagem(self, msg: str):
        print(msg)

    def seleciona_cidade(self) -> str:
        return input("Informe o nome da cidade do local: ")

    def seleciona_passeio(self) -> str:
        return input("Informe o nome do passeio que deseja adicionar: ")

    def mostra_local(self, dados: dict):
        print(f"Local: {dados['cidade']}")
        if dados['passeios']:
            print("   Passeios disponíveis:")
            for passeio in dados['passeios']:
                print(f"     - {passeio}")
        else:
            print("Nenhum passeio associado a este local")
