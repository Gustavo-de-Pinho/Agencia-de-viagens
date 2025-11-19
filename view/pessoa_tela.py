import FreeSimpleGUI as sg


class PessoaTela:
    def __init__(self):
        self.__window_menu = None

    def mostra_opcoes(self):
        '''print("======= OPÇÕES =======")
        print("> (1) Adicionar Pessoa no Sistema")
        print("> (2) Remover Pessoa do Sistema")
        print("> (3) Editar Informações de Pessoa")
        print("> (4) Listar pessoas no Sistema")
        print("> (0) Retonar")
        print("======================")
        print()

        opcao = input("Escolha uma opção: ")

        try:
            opcao = int(opcao)
            return opcao
        except:
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("OPÇÕES DE PESSOA"), sg.Push()],
            [sg.Button("Adicionar pessoa no Sistema", key=1)],
            [sg.Button("Remover pessoa do Sistema", key=2)],
            [sg.Button("Editar Informações de Pessoa", key=3)],
            [sg.Button("Listar pessoas no Sistema", key=4)],
            [sg.Cancel("Retornar", key=0)]
        ]

        if self.__window_menu is None:
            self.__window_menu = sg.Window("OPÇÕES DE PESSOA", layout=layout, size=(400, 200))

        while True:
            event, values = self.__window_menu.read()

            if event == 0:
                self.__window_menu.close()
                self.__window_menu = None

            return event
        
    def pega_info_pessoa(self):
        '''nome = input("> Nome: ")
        data_nascimento = input("> Data de nascimento (DD-MM-AAAA): ")
        cpf = input("> CPF: ")
        telefone = input("> Telefone: ")

        if isinstance(nome, str) and isinstance(data_nascimento, str) and isinstance(cpf, str) and isinstance(telefone, str):
            return {
                "nome": nome,
                "data_nascimento": data_nascimento,
                "cpf": cpf,
                "telefone": telefone}
        else:
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("INFORMAÇÕES DA PESSOA"), sg.Push()],
            [sg.Text("Nome"), sg.InputText(key="nome")],
            [sg.Text("Data de nascimento (DD-MM-AAAA)"), sg.InputText(key="data_nascimento")],
            [sg.Text("CPF"), sg.InputText(key="cpf")],
            [sg.Text("Telefone"), sg.InputText(key="telefone")],
            [sg.Submit()]
        ]

        window = sg.Window("Pessoa", layout=layout, size=(400, 200))

        botao, dados_dict = window.Read()
        window.close()

        if isinstance(dados_dict["nome"], str) and isinstance(dados_dict["data_nascimento"], str) \
        and isinstance(dados_dict["cpf"], str) and isinstance(dados_dict["telefone"], str):
                return dados_dict
        else:
            return None

    def pega_cpf_pessoa(self):
        '''cpf = input("> CPF: ")

        if isinstance(cpf, str):
            return cpf
        else:
            return None'''
        
        layout = [
            [sg.Text("CPF DA PESSOA")],
            [sg.Text("CPF"), sg.InputText(key="cpf")],
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

        '''novo_nome = input("> Novo Nome: ")
        nova_data_nascimento = input("> Nova Data de Nascimento: ")
        novo_telefone = input("> Novo Telefone: ")

        if cpf is not None and isinstance(novo_nome, str) and isinstance(nova_data_nascimento, str) and isinstance(novo_telefone, str):
            return {
                "nome": novo_nome,
                "data_nascimento": nova_data_nascimento,
                "cpf": cpf,
                "telefone": novo_telefone
            }
        else:
            return None'''
        
        layout = [
            [sg.Text("INFORMAÇÕES NOVAS")],
            [sg.Text("Novo nome"), sg.InputText(key="nome")],
            [sg.Text("Nova data de nascimento"), sg.InputText(key="data_nascimento")],
            [sg.Text("Novo telefone"), sg.InputText(key="telefone")],
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

    def mostrar_pessoa(self, pessoa):
        print("=======================")
        print(f"> Nome: {pessoa['nome']}")
        print(f"> Data de Nascimento: {pessoa['data_nascimento']}")
        print(f"> CPF: {pessoa['cpf']}")
        print(f"> Telefone: {pessoa['telefone']}")
        print("=======================")

        '''layout = [
            [sg.Text(f"Nome: {pessoa["nome"]}")],
            [sg.Text(f"Data de Nascimento: {pessoa["data_nascimento"]}")],
            [sg.Text(f"CPF: {pessoa["cpf"]}")],
            [sg.Text(f"Telefone: {pessoa["telefone"]}")],
            [sg.Cancel("Retornar")]
        ]

        sg.Window("Pessoa", layout=layout)'''

    def mostra_mensagem(self, msg):
        sg.Popup(msg)
