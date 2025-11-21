import FreeSimpleGUI as sg

class CidadeTela:
    def __init__(self):
        self.__window_menu = None

    def mostra_opcoes(self) -> int:
        layout = [
            [sg.Text('------ GERENCIAMENTO ------', font=('Helvetica', 12, 'bold'), justification='center', expand_x=True)],
            [sg.Text('PAÍS', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Cadastrar País', key='1', size=(15,1)), sg.Button('Alterar País', key='2', size=(15,1))],
            [sg.Button('Listar Países', key='3', size=(15,1)), sg.Button('Excluir País', key='4', size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Text('CIDADE', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Cadastrar Cidade', key='5', size=(15,1)), sg.Button('Alterar Cidade', key='6', size=(15,1))],
            [sg.Button('Listar Cidades', key='7', size=(15,1)), sg.Button('Excluir Cidade', key='8', size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Button('Sair', key='0', button_color=('white', 'firebrick3'), size=(32,1))]
        ]

        window = sg.Window('Menu Principal', layout, element_justification='c')

        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, '0'):
            return 0

        return int(event)

    def mostra_mensagem(self, msg: str):
        sg.popup(msg, title="Mensagem")

    # --- Métodos para País ---
    def pega_dados_pais(self) -> str:
        layout = [
            [sg.Text('Digite os dados do País')],
            [sg.Text('Nome:', size=(10, 1)), sg.InputText(key='nome')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Cadastro de País', layout)
        
        event, values = window.read()
        window.close()
        
        if event == 'Confirmar':
            return values['nome']
        return "" 
    
    def mostra_pais(self, dados: dict):
        mensagem = f"ID: {dados['id']}\nNome: {dados['nome']}"
        sg.popup(mensagem, title="Dados do País")
        
    def mostra_lista_paises(self, dados_paises):
        string_todos_paises = ""
        for dado in dados_paises:
            string_todos_paises += "ID: " + str(dado.id) + '\n'
            string_todos_paises += "NOME: " + str(dado.nome) + '\n\n'

        sg.Popup('-------- LISTA DE PAISES ----------', string_todos_paises, non_blocking = True)

    def seleciona_pais_id(self) -> int:
        while True:
            layout = [
                [sg.Text('Informe o ID do País:')],
                [sg.InputText(key='id')],
                [sg.Button('OK'), sg.Button('Cancelar')]
            ]
            window = sg.Window('Selecionar País', layout)
            event, values = window.read()
            window.close()

            if event in (sg.WIN_CLOSED, 'Cancelar'):
                return 0 # Ou lidar com cancelamento como preferir
            
            try:
                return int(values['id'])
            except ValueError:
                sg.popup_error("ERRO: O ID deve ser um número inteiro.")

    # --- Métodos para Cidade ---
    def pega_dados_cidade(self) -> str:
        layout = [
            [sg.Text('Digite os dados da Cidade')],
            [sg.Text('Nome:', size=(10, 1)), sg.InputText(key='nome')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Cadastro de Cidade', layout)
        
        event, values = window.read()
        window.close()
        
        if event == 'Confirmar':
            return values['nome']
        return ""

    def mostra_cidade(self, dados: dict):
        mensagem = f"ID: {dados['id_cidade']}\nCidade: {dados['nome_cidade']}\nPaís: {dados['nome_pais']}"
        sg.popup(mensagem, title="Dados da Cidade")
        
    def mostra_lista_cidades(self, dados_cidades):
        string_todas_cidades = ""
        for dado in dados_cidades:
            string_todas_cidades += "ID: " + str(dado.id) + '\n'
            string_todas_cidades += "NOME: " + str(dado.nome) + '\n\n'

        sg.Popup('-------- LISTA DE CIDADES ----------', string_todas_cidades, non_blocking = True)

    def seleciona_cidade_id(self) -> int:
        while True:
            layout = [
                [sg.Text('Informe o ID da Cidade:')],
                [sg.InputText(key='id')],
                [sg.Button('OK'), sg.Button('Cancelar')]
            ]
            window = sg.Window('Selecionar Cidade', layout)
            event, values = window.read()
            window.close()

            if event in (sg.WIN_CLOSED, 'Cancelar'):
                return 0
            
            try:
                return int(values['id'])
            except ValueError:
                sg.popup_error("ERRO: O ID deve ser um número inteiro.")
    
    
    '''def mostra_opcoes(self) -> int:
        print("===========================")
        print("---------- PAÍS -----------")
        print("> (1) Cadastrar País")
        print("> (2) Alterar País")
        print("> (3) Listar Países")
        print("> (4) Excluir País")
        print("---------- CIDADE ----------")
        print("> (5) Cadastrar Cidade")
        print("> (6) Alterar Cidade")
        print("> (7) Listar Cidades")
        print("> (8) Excluir Cidade")
        print("---------------------------")
        print("> (0) Retornar")
        print("===========================")
        print()
        
        try:
            return int(input("Escolha uma opção: "))
        except:
            return None
    
    def mostra_mensagem(self, msg: str):
        print(msg)

    # --- Métodos para País ---
    def pega_dados_pais(self) -> str:
        print("\n-- DADOS DO PAÍS --")
        return input("Nome: ")

    def mostra_pais(self, dados: dict):
        print(f"  > ID: {dados['id']} - {dados['nome']}")

    def seleciona_pais_id(self) -> int:
        while True:
            try:
                id_pais = int(input("Informe o ID do país: "))
                return id_pais
            except ValueError:
                print("ERRO: O ID deve ser um número inteiro.")

    # --- Métodos para Cidade ---
    def pega_dados_cidade(self) -> str:
        print("\n-- DADOS DA CIDADE --")
        return input("Nome: ")

    def mostra_cidade(self, dados: dict):
        print(f"  > ID: {dados['id_cidade']} - Cidade: {dados['nome_cidade']} | País: {dados['nome_pais']}")

    def seleciona_cidade_id(self) -> int:
        while True:
            try:
                id_cidade = int(input("Informe o ID da cidade: "))
                return id_cidade
            except ValueError:
                print("ERRO: O ID deve ser um número inteiro.")'''