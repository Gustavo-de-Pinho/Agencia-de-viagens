import FreeSimpleGUI as sg


class PacoteTela:
    def __init__(self):
        self.__window_menu = None
        self.__window_edicao_menu = None

    def opcoes(self):
        
        layout = [
            [sg.Text("------ GERENCIAMENTO ------", font=("Helvetica", 12, "bold"), justification="center", expand_x=True)],
            [sg.Push(), sg.Text("Pacote"), sg.Push()],
            [sg.Button("Criar Pacote", key=1, size=(15, 1)), sg.Button("Editar Pacote", key=2, size=(15, 1))],
            [sg.Button("Histórico de Pacotes", key=3, size=(15, 1)), sg.Button("Excluir Pacote", key=4, size=(15, 1))],
            [sg.Push(), sg.Cancel("Retonar", key=0, size=(15, 1), button_color=("white", "firebrick3")), sg.Push()]
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

        layout = [
            [sg.Push(), sg.Text("------ CRIAR PACOTE ------"), sg.Push()],
            [sg.Text("Código do grupo"), sg.Push(), sg.InputText(key="codigo", size=(32, 1))],
            [sg.Text("Data da viagem (DD-MM-AAAA)"), sg.Push(), sg.InputText(key="data", size=(32, 1))],
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

        layout = [
            [sg.Push(), sg.Text("------ EDITAR PACOTE ------"), sg.Push()],
            [sg.Push(), sg.Button("Adicionar Passagens", key=1, size=(20, 1)), sg.Push()],
            [sg.Push(), sg.Button("Criar Itinerário", key=2, size=(20, 1)), sg.Push()],
            [sg.Push(), sg.Cancel("Retornar", key=0, button_color=("white", "firebrick3"), size=(15, 1)), sg.Push()]
        ]

        if self.__window_edicao_menu is None:
            self.__window_edicao_menu = sg.Window("EDITAR PACOTE", layout=layout)
        
        while True:
            event, values = self.__window_edicao_menu.read()

            if event == 0 or event == sg.WIN_CLOSED:
                self.__window_edicao_menu.close()
                self.__window_edicao_menu = None

            return event

    def adicionar_passagem(self):

        layout = [
            [sg.Push(), sg.Text("------ ADICIONAR PASSAGEM ------"), sg.Push()],
            [sg.Text("Código do grupo"), sg.Push(), sg.InputText(key="codigo", size=(32, 1))],
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

        layout = [
            [sg.Push(), sg.Text("------ CRIAR ITINERÁRIO ------"), sg.Push()],
            [sg.Text("Código do grupo"), sg.Push(), sg.InputText(key="codigo", size=(32, 1))],
            [sg.Text("Dias de viagem"), sg.Push(), sg.InputText(key="dias", size=(32, 1))],
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

        layout = [
            [sg.Push(), sg.Text(f"------ DIA {dia} ------"), sg.Push()],
            [sg.Text("Cidade"), sg.Push(), sg.InputText(key="cidade", size=(32, 1))],
            [sg.Text("Passeio (se houver)"), sg.Push(), sg.InputText(key="passeio", size=(32, 1))],
            [sg.Submit()]
        ]

        window = sg.Window("Pacote", layout=layout)

        botao, dados_dict = window.read()
        window.close()

        if dados_dict["passeio"] is None:
            dados_dict["passeio"] = ""
        
        return dados_dict
    
    def historico_pacotes(self):

        layout = [
            [sg.Push(), sg.Text("------ HISTÓRICO DE PACOTES ------"), sg.Push()],
            [sg.Text("Código do grupo"), sg.Push(), sg.InputText(key="codigo", size=(32, 1))],
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
    
    def mostrar_pacotes(self, dados_pacotes: list):

        pacotes_string = ""

        for pacote in dados_pacotes:
            pacotes_string += f"Valor total: {pacote["valor_total"]}\n"
            pacotes_string += f"Valor pago: {pacote["valor_pago"]}\n"
            pacotes_string += f"Pacote pago? {pacote["pago"]}\n"
    
            pacotes_string += f"Passagens: \n"
            for passagem in pacote["passagens"]:
                pacotes_string += f"{passagem}\n"
            
            pacotes_string += "Itinerário: \n"
            for dia in pacote["itinerario"]:
                pacotes_string += f"{dia}\n"

            pacotes_string += "\n"

        sg.Popup("------ HISTÓRICO DE PACOTES ------\n", pacotes_string)

    def excluir_pacote(self):

        layout = [
            [sg.Push(), sg.Text("------ EXCLUIR PACOTE ------"), sg.Push()],
            [sg.Text("Código do grupo"), sg.Push(), sg.InputText(key="codigo", size=(32, 1))],
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

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)