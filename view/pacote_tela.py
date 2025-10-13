class PacoteTela:
    def opcoes(self):
        print("====== OPÇÕES ======")
        print("> (1) Criar Pacote")
        print("> (2) Editar Pacote")
        print("> (3) Histórico de Pacotes")
        print("> (4) Excluir Pacote")
        print("> (0) Retornar")
        print("====================")
        print()

        opcao = input("Escolha uma opção: ")

        try:
            opcao = int(opcao)
            return opcao
        except:
            return None
        
    def criar_pacote(self):
        print("====== CRIAR PACOTE ======")
        codigo = input("> Código do grupo: ")
        data = input("> Data da viagem (DD-MM-AAAA): ")
        print("==========================")

        try:
            codigo = int(codigo)
            return {"codigo": codigo, "data": data}
        except:
            return None
    
    def editar_pacote(self):
        print("====== EDITAR PACOTE ======")
        print("> (1) ADICIONAR PASSAGENS")
        print("> (2) CRIAR ITINERÁRIO")
        print("> (0) RETORNAR")
        print("===========================")

        opcao = input("Escolha uma opção: ")

        try:
            opcao = int(opcao)
            return opcao
        except:
            return None
        
    def adicionar_passagem(self):
        print("====== ADICIONAR PASSAGEM ======")
        codigo = input("> Código do grupo: ")
        print("================================")

        try:
            codigo = int(codigo)
            print("RETORNOU INT")
            return codigo
        except:
            print("RETORNOU NONE")
            return None
        
    def criar_itinerario(self):
        print("====== CRIAR ITINERÁRIO ======")
        codigo = input("> Código do grupo: ")
        dias = input("> Quantidade de dias: ")
        print("==============================")

        try:
            if dias is not None and codigo is not None:
                dias = int(dias)
                codigo = int(codigo)
                return {"codigo": codigo, "dias": dias}
            else:
                return None
        except: 
            return None

    def dia_itinerario(self, dia):
        dia_dict = {}
        print(f"====== DIA {dia} ======")
        dia_dict['cidade'] = input('> Cidade: ')
        dia_dict['passeio'] = input('> Passeio (Se houver): ')
        print("========================")

        if not dia_dict["passeio"]:
            dia_dict["passeio"] = ""

        return dia_dict
    
    def historico_pacotes(self):
        print("====== HISTÓRICO DE PACOTES ======")
        codigo = input("> Código do grupo: ")
        print("==================================")

        try:
            codigo = int(codigo)
            return codigo
        except:
            return None
    
    def mostrar_pacote(self, pacote_dict):
        print("============================================")
        print(f"> Valor total: {pacote_dict["valor_total"]}")
        print(f"> Valor pago: {pacote_dict["valor_pago"]}")
        print(f"> Pacote pago? {pacote_dict["pago"]}")
        print(f"> Passagens:")
        for passagem in pacote_dict["passagens"]:
            print(passagem)
        print(f"> Itinerário:")
        for dia in pacote_dict["itinerario"]:
            print(dia)
        print("============================================")

    def excluir_pacote(self):
        print("====== EXCLUIR PACOTE ======")
        codigo = input("> Código do grupo: ")
        print("============================")

        try:
            codigo = int(codigo)
            return codigo
        except:
            return None

    def mostrar_mensagem(self, msg):
        print(msg)