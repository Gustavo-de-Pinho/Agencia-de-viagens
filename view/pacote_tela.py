import FreeSimpleGUI as sg


class PacoteTela:
    def __init__(self):
        self.__window_menu = None
        self.__window_edicao_menu = None

    def opcoes(self):
        '''print("====== OPÇÕES ======")
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
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("OPÇÕES DE PACOTE"), sg.Push()],
            [sg.Button("Criar Pacote", key=1)],
            [sg.Button("Editar Pacote", key=2)],
            [sg.Button("Histórico de Pacotes", key=3)],
            [sg.Button("Excluir Pacote", key=4)],
            [sg.Cancel("Retonar", key=0)]
        ]

        if self.__window_menu is None:
            self.__window_menu = sg.Window("OPÇÕES DE PACOTE", layout=layout)

        while True:
            event, values = self.__window_menu.read()

            if event == 0 or event == sg.WIN_CLOSED:
                self.__window_menu.close()
                self.__window_menu = None

            return event
        
    def criar_pacote(self):
        '''print("====== CRIAR PACOTE ======")
        codigo = input("> Código do grupo: ")
        data = input("> Data da viagem (DD-MM-AAAA): ")
        print("==========================")

        try:
            codigo = int(codigo)
            return {"codigo": codigo, "data": data}
        except:
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("CRIAR PACOTE"), sg.Push()],
            [sg.Text("Código do grupo"), sg.InputText(key="codigo")],
            [sg.Text("Data da viagem (DD-MM-AAAA)"), sg.InputText(key="data")],
            [sg.Submit()]
        ]

        window = sg.Window("Pacote", layout=layout)

        botao, dados_dict = window.read()
        window.close()

        try:
            dados_dict["codigo"] = int(dados_dict["codigo"])
            return dados_dict
        except:
            return None
    
    def editar_pacote(self):
        '''print("====== EDITAR PACOTE ======")
        print("> (1) ADICIONAR PASSAGENS")
        print("> (2) CRIAR ITINERÁRIO")
        print("> (0) RETORNAR")
        print("===========================")

        opcao = input("Escolha uma opção: ")

        try:
            opcao = int(opcao)
            return opcao
        except:
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("EDITAR PACOTE"), sg.Push()],
            [sg.Button("Adicionar Passagens", key=1)],
            [sg.Button("Criar Itinerário", key=2)],
            [sg.Cancel("Retornar", key=0)]
        ]

        if self.__window_edicao_menu is None:
            self.__window_edicao_menu = sg.Window("EDITAR PACOTE", layout=layout)
        
        while True:
            event, values = self.__window_edicao_menu.read()

            if event == 0 or event == sg.WIN_CLOSED:
                self.__window_edicao_menu.close()
                self.__window_menu = None

            return event

    def adicionar_passagem(self):
        '''print("====== ADICIONAR PASSAGEM ======")
        codigo = input("> Código do grupo: ")
        print("================================")

        try:
            codigo = int(codigo)
            return codigo
        except:
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("ADICIONAR PASSAGEM"), sg.Push()],
            [sg.Text("Código do grupo"), sg.InputText(key="codigo")],
            [sg.Submit()]
        ]

        window = sg.Window("Pacote", layout=layout)

        botao, dados_dict = window.read()
        window.close()

        try:
            dados_dict["codigo"] = int(dados_dict["codigo"])
            return dados_dict["codigo"]
        except:
            return None
        
    def criar_itinerario(self):
        '''print("====== CRIAR ITINERÁRIO ======")
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
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("CRIAR ITINERÁRIO"), sg.Push()],
            [sg.Text("Código do grupo"), sg.InputText(key="codigo")],
            [sg.Text("Dias de viagem"), sg.InputText(key="dias")]
            [sg.Submit()]
        ]

        window = sg.Window("Pacote", layout=layout)

        botao, dados_dict = window.read()
        window.close()

        try:
            dados_dict["dias"] = int(dados_dict["dias"])
            dados_dict["codigo"] = int(dados_dict["codigo"])
            return dados_dict
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

        '''layout = [
            [sg.Push(), sg.Text(f"DIA {dia}")]
        ]'''
    
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