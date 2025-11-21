import FreeSimpleGUI as sg


class PessoaTela:
    def __init__(self):
        self.__window_menu = None

    def mostra_opcoes(self):
        
        layout = [
            [sg.Text("------ GERENCIAMENTO ------", font=("Helvetica", 12, "bold"), justification="center", expand_x=True)],
            [sg.Text("Pessoa", justification="center", expand_x=True)],
            [sg.Button("Adicionar pessoa", key=1, size=(15, 1)), sg.Button("Remover pessoa", key=2, size=(15, 1))],
            [sg.Button("Editar Informações", key=3, size=(15, 1)), sg.Button("Listar pessoas", key=4, size=(15, 1))],
            [sg.Push(), sg.Cancel("Retornar", key=0, button_color=("white", "firebrick3"), size=(15, 1)), sg.Push()]
        ]

        if self.__window_menu is None:
            self.__window_menu = sg.Window("OPÇÕES DE PESSOA", layout=layout)

        while True:
            event, values = self.__window_menu.read()

            if event == 0 or event == sg.WIN_CLOSED:
                self.__window_menu.close()
                self.__window_menu = None
                return 0

            return event
        
    def pega_info_pessoa(self):

        layout = [
            [sg.Push(), sg.Text("------ INFORMAÇÕES DA PESSOA ------"), sg.Push()],
            [sg.Text("Nome"), sg.Push(), sg.InputText(key="nome", size=(32, 1))],
            [sg.Text("Data de nascimento (DD-MM-AAAA)"), sg.Push(), sg.InputText(key="data_nascimento", size = (32, 1))],
            [sg.Text("CPF"), sg.Push(), sg.InputText(key="cpf", size=(32, 1))],
            [sg.Text("Telefone"), sg.Push(), sg.InputText(key="telefone", size=(32, 1))],
            [sg.Submit()]
        ]

        window = sg.Window("Pessoa", layout=layout)

        botao, dados_dict = window.Read()
        window.close()

        if isinstance(dados_dict["nome"], str) and isinstance(dados_dict["data_nascimento"], str) \
        and isinstance(dados_dict["cpf"], str) and isinstance(dados_dict["telefone"], str):
                return dados_dict
        else:
            return None

    def pega_cpf_pessoa(self):

        layout = [
            [sg.Text("------ CPF DA PESSOA ------", justification="center", expand_x=True)],
            [sg.Text("CPF"), sg.Push(), sg.InputText(key="cpf", size=(32, 1))],
            [sg.Submit()]
        ]

        window = sg.Window("Pessoa", layout=layout)

        botao, dados_dict = window.Read()
        window.close()

        if isinstance(dados_dict["cpf"], str):
            return dados_dict["cpf"]
        else:
            return None

    def inclui_pessoa(self):
        dados = self.pega_info_pessoa()

        return dados
        
    def remove_pessoa(self):
        cpf = self.pega_cpf_pessoa()

        return cpf
        
    def edita_info_pessoa(self):
        cpf = self.pega_cpf_pessoa()

        layout = [
            [sg.Text("------ INFORMAÇÕES NOVAS ------", justification="center", expand_x=True)],
            [sg.Text("Novo nome"), sg.Push(), sg.InputText(key="nome", size=(32, 1))],
            [sg.Text("Nova data de nascimento"), sg.Push(), sg.InputText(key="data_nascimento", size=(32, 1))],
            [sg.Text("Novo telefone"), sg.Push(), sg.InputText(key="telefone", size=(32, 1))],
            [sg.Submit()]
        ]

        window = sg.Window("Pessoa", layout=layout)

        botao, dados_dict = window.Read()
        window.close()

        if cpf is not None and isinstance(dados_dict["nome"], str) and isinstance(dados_dict["data_nascimento"], str) \
        and isinstance(dados_dict["telefone"], str):
            dados_dict["cpf"] = cpf
            return dados_dict
        else:
            return None

    def mostrar_pessoas(self, dados_pessoas: list):

        string_pessoas = ""

        for pessoa in dados_pessoas:
            string_pessoas += f"Nome: {pessoa["nome"]}\n"
            string_pessoas += f"Data de Nascimento: {pessoa["data_nascimento"]}\n"
            string_pessoas += f"CPF: {pessoa["cpf"]}\n"
            string_pessoas += f"Telefone: {pessoa["telefone"]}\n\n"

        sg.Popup("------ LISTA DE PESSOAS ------\n", string_pessoas, non_blocking = True)

    def mostra_mensagem(self, msg):
        sg.Popup(msg)
