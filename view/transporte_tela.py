class TransporteTela:
    def mostra_opcoes(self):
        print("======= TRANSPORTES =======")
        print("-------- EMPRESA ---------")        
        print("> (1) Cadastrar empresa")
        print("> (2) Alterar empresa")
        print("> (3) Listar empresas")
        print("> (4) Excluir empresa")
        print("------ TRANSPORTE -------")  
        print("> (5) Cadastrar transporte")
        print("> (6) Alterar transporte")
        print("> (7) Listar transportes")
        print("> (8) Excluir transporte")
        print("-------------------------")  
        print("> (0) Retornar")
        print("===========================")
        print()
        
        try:
            return int(input("Escolha uma opção: "))
        except:
            return None
        
    def mostra_mensagem(self, msg):
        print(msg)

    def pega_dados_empresa(self):
        print("\n-- DADOS EMPRESA --")
        nome = input("Nome: ")
        cnpj = input("CNPJ: ")
        return {"nome": nome, "cnpj": cnpj}

    def mostra_empresa(self, dados):
        print(f"  {dados['nome']}  |  CNPJ: {dados['cnpj']}")

    def seleciona_empresa(self):
        return input("Informe o CNPJ da empresa: ")

    def pega_meio_locomocao(self):
        return input("Meio de locomoção: ")

    def mostra_transporte(self, dados):
        print(f" ID: {dados['id']} | Empresa: {dados['empresa']}  |  CNPJ: {dados['cnpj']}  |  Locomoção: {dados['meio']}")

    def seleciona_transporte(self):
        try:
            return int(input("ID do transporte (número): "))
        except: 
            return None
