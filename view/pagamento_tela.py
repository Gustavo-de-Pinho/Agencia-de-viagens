class PagamentoTela:
    def mostrar_opcoes(self):
        print("======= OPÇÕES =======")
        print("> (1) Realizar Pagamento")
        print("> (2) Histórico de Pagamentos")
        print("> (0) Retornar")
        print("======================")
        print()

        opcao = input("Escolha uma opção: ")

        try:
            opcao = int(opcao)
            return opcao
        except:
            return None
        
    def pagamento_padrao_dados(self):
        cpf = input("> CPF do Membro: ")
        codigo = input("> Código do Grupo: ")
        valor = input("> Valor do pagamento: ")

        try:
            valor = float(valor)
            codigo = int(codigo)
            return {"cpf_membro": cpf, "codigo": codigo, "valor": valor}
        except:
            return None
        
    def realizar_pagamento(self):
        print("======= REALIZAR PAGAMENTO =======")
        print("> (1) PIX")
        print("> (2) Cartão de Crédito")
        print("> (3) Dinheiro")
        print("> (0) Retornar")
        print("==================================")

        opcao = input("Escolha uma opcao: ")

        try:
            opcao = int(opcao)
            return opcao
        except:
            return None

    def pagamento_pix(self):
        print("======= PAGAMENTO PIX =======")
        dados = self.pagamento_padrao_dados()
        if dados is not None:
            dados["cpf_pagador"] = input("> CPF do Pagador: ")
        print("=============================")

        return dados

        
    def pagamento_cartao(self):
        print("======= PAGAMENTO CARTÃO =======")
        dados = self.pagamento_padrao_dados()
        if dados is not None:
            dados["numero_cartao"] = input("> Número do Cartão: ")
            dados["bandeira"] = input("> Bandeira do Cartão: ")
        print("=================================")

        return dados

    def pagamento_dinheiro(self):
        print("======= PAGAMENTO DINHEIRO =======")
        dados = self.pagamento_padrao_dados()
        print("==================================")

        return dados
    
    def pegar_cpf_lista(self):
        print("====== LISTAR PAGAMENTOS ======")
        cpf = input("> CPF: ")
        print("===============================")

        return cpf
    
    def listar_pagamentos(self, pagamento_dict: dict):
        print("========================")
        for key in pagamento_dict:
            print(f"> {pagamento_dict[key]}")
        print("========================")

    def mostrar_mensagem(self, msg):
        print(msg)