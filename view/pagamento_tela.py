import FreeSimpleGUI as sg


class PagamentoTela:
    def __init__(self):
        self.__window_menu = None
        self.__window_menu_pagamento = None

    def mostrar_opcoes(self):
        
        layout = [
            [sg.Text("------ GERENCIAMENTO ------", font=("Helvetica", 12, "bold"), justification="center", expand_x=True)],
            [sg.Text("Pagamento", justification="c", expand_x=True)],
            [sg.Push(), sg.Button("Realizar Pagamento", key=1, size=(20, 2)), sg.Push()],
            [sg.Push(), sg.Button("Histórico de Pagamentos", key=2, size=(20, 2)), sg.Push()],
            [sg.Push(), sg.Button("Retornar", key=0, size=(15, 1), button_color=("white", "firebrick3")), sg.Push()]
        ]
        
        if self.__window_menu is None:
            self.__window_menu = sg.Window("OPÇÕES PAGAMENTO", layout=layout)

        while True:
            event, values = self.__window_menu.read()

            if event == 0 or event == sg.WIN_CLOSED:
                self.__window_menu.close()
                self.__window_menu = None
                return 0

            return event
        
    def pagamento_padrao_dados(self):
        
        layout = [
            [sg.Text("------ DADOS PADRÕES DE PAGAMENTO ------", justification="c", expand_x=True)],
            [sg.Text("CPF do Membro"), sg.Push(), sg.InputText(key="cpf_membro", size=(32, 1))],
            [sg.Text("Código do Grupo"), sg.Push(), sg.InputText(key="codigo", size=(32, 1))],
            [sg.Text("Valor do pagamento"), sg.Push(), sg.InputText(key="valor", size=(32, 1))],
            [sg.Submit()]
        ]

        window = sg.Window("Pagamento", layout=layout)

        botao, dados_dict = window.read()
        window.close()

        try:
            dados_dict["valor"] = float(dados_dict["valor"])
            dados_dict["codigo"] = int(dados_dict["codigo"])
            return dados_dict
        except:
            return None
        
    def realizar_pagamento(self):
        
        layout = [
            [sg.Text("------ REALIZAR PAGAMENTO ------", justification="c", expand_x=True)],
            [sg.Push(), sg.Button("PIX", key=1, size=(15, 1)), sg.Push()],
            [sg.Push(), sg.Button("Cartão de Crédito", key=2, size=(15, 1)), sg.Push()],
            [sg.Push(), sg.Button("Dinheiro", key=3, size=(15, 1)), sg.Push()],
            [sg.Push(), sg.Cancel("Retornar", key=0, button_color=("white", "firebrick3")), sg.Push()]
        ]

        if self.__window_menu_pagamento is None:
            self.__window_menu_pagamento = sg.Window("Pagamento", layout=layout)

        while True:
            event, values = self.__window_menu_pagamento.read()

            if event == 0 or event == sg.WIN_CLOSED:
                self.__window_menu_pagamento.close()
                self.__window_menu_pagamento = None
                return 0

            return event

    def pagamento_pix(self):
        dados = self.pagamento_padrao_dados()
        
        layout = [
            [sg.Text("------ PAGAMENTO PIX ------", justification="c", expand_x=True)],
            [sg.Text("CPF do Pagador"), sg.Push(), sg.InputText(key="cpf_pagador", size=(32, 1))],
            [sg.Submit()]
        ]

        if dados is not None:
            window = sg.Window("Pagamento", layout=layout)

            botao, dados_dict = window.read()
            window.close()

            dados["cpf_pagador"] = dados_dict["cpf_pagador"]

        return dados

        
    def pagamento_cartao(self):
        dados = self.pagamento_padrao_dados()
        
        layout = [
            [sg.Text("------ PAGAMENTO CARTÃO DE CŔEDITO ------", justification="c", expand_x=True)],
            [sg.Text("Número do Cartão"), sg.Push(), sg.InputText(key="numero_cartao", size=(32, 1))],
            [sg.Text("Bandeira do Cartão"), sg.Push(), sg.InputText(key="bandeira", size=(32, 1))],
            [sg.Submit()]
        ]

        if dados is not None:
            window = sg.Window("Pagamento", layout=layout)

            botao, dados_dict = window.read()
            window.close()

            dados["numero_cartao"] = dados_dict["numero_cartao"]
            dados["bandeira"] = dados_dict["bandeira"]

        return dados

    def pagamento_dinheiro(self):
        dados = self.pagamento_padrao_dados()

        return dados
    
    def pegar_cpf_lista(self):

        layout = [
            [sg.Text("------ LISTAR PAGAMENTOS ------", justification="c", expand_x=True)],
            [sg.Text("CPF"), sg.Push(), sg.InputText(key="cpf", size=(32, 1))],
            [sg.Submit()]
        ]

        window = sg.Window("Pagamento", layout=layout)

        botao, dados_dict = window.read()
        window.close()

        return dados_dict["cpf"]
    
    def listar_pagamentos(self, dados_pagamentos: list):

        string_pagamentos = ''

        for pagamento in dados_pagamentos:
            for key in pagamento:
                string_pagamentos += f"> {pagamento[key]}\n"
            string_pagamentos += "\n"

        sg.Popup("------ PAGAMENTOS ------\n", string_pagamentos)

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)