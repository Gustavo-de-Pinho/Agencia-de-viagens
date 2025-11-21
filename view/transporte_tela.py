import FreeSimpleGUI as sg

class TransporteTela:
    def __init__(self):
        self.__window_menu = None

    def mostra_opcoes(self) -> int:
        layout = [
            [sg.Text('------ GERENCIAMENTO ------', font=('Helvetica', 12, 'bold'), justification='center', expand_x=True)],
            [sg.Text('--EMPRESA--', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Cadastrar Empresa', key='1', size=(15,1)), sg.Button('Alterar Empresa', key='2', size=(15,1))],
            [sg.Button('Listar Empresas', key='3', size=(15,1)), sg.Button('Excluir Empresa', key='4', size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Text('--TRANSPORTE--', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Cadastrar Transporte', key='5', size=(15,1)), sg.Button('Alterar Transporte', key='6', size=(15,1))],
            [sg.Button('Listar Transportes', key='7', size=(15,1)), sg.Button('Excluir Transporte', key='8', size=(15,1))],
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
        
    def pega_dados_empresa(self):
        layout = [
            [sg.Text('-------- DADOS EMPRESA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Cadastro de Emprsae', layout)
        
        event, values = window.read()
        window.close()
        
        if event == 'Confirmar':
            return {"nome": values['nome'], "cnpj": values['cnpj']}
        return ""
    
    def mostra_empresa(self, dados: dict):
        mensagem = f"CNPJ: {dados['cnpj']}\nEmpresa: {dados['nome']}"
        sg.popup(mensagem, title="Dados da Empresa")
        
    def mostra_lista_empresas(self, dados_empresas):
        string_todas_empresas = ""
        for dado in dados_empresas:
            string_todas_empresas += "NOME: " + str(dado.nome) + '\n'
            string_todas_empresas += "CNPJ: " + str(dado.cnpj) + '\n\n'

        sg.Popup('-------- LISTA DE EMPRESAS ----------', string_todas_empresas, non_blocking = True)
        
    def seleciona_empresa(self) -> int:
        while True:
            layout = [
                [sg.Text('Informe o CNPJ da Empresa:')],
                [sg.InputText(key='cnpj')],
                [sg.Button('OK'), sg.Button('Cancelar')]
            ]
            window = sg.Window('Selecionar Empresa', layout)
            event, values = window.read()
            window.close()

            if event in (sg.WIN_CLOSED, 'Cancelar'):
                return 0
            
            try:
                return str(values['cnpj'])
            except ValueError:
                sg.popup_error("ERRO: CNPJ inválido.")
    
    def pega_meio_locomocao(self):
        layout = [
            [sg.Text('-------- DADOS LOCOMOçÃO ----------', font=("Helvica", 25))],
            [sg.Text('Locomoção:', size=(15, 1)), sg.InputText('', key='locomocao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Cadastro de Cidade', layout)
        
        event, values = window.read()
        window.close()
        
        if event == 'Confirmar':
            return values['locomocao']
        return ""
    
    def mostra_transporte(self, dados: dict):
        mensagem = f"ID: {dados['id']}\nLocomoçao: {dados['meio']}"
        sg.popup(mensagem, title="Dados Transporte")
                
    def mostra_lista_transporte(self, dados_transporte):
        string_todos_transportes = ""
        for dado in dados_transporte:
            string_todos_transportes += "ID: " + str(dado.id) + '\n'
            string_todos_transportes += "Locomocao: " + str(dado.meio_locomocao) + '\n\n'

        sg.Popup('-------- LISTA DE TRANSPORTES ----------', string_todos_transportes, non_blocking = True)
        
    def seleciona_transporte(self) -> int:
        while True:
            layout = [
                [sg.Text('Informe o ID do trasnsporte: ')],
                [sg.InputText(key='id')],
                [sg.Button('OK'), sg.Button('Cancelar')]
            ]
            window = sg.Window('Selecionar Transporte', layout)
            event, values = window.read()
            window.close()

            if event in (sg.WIN_CLOSED, 'Cancelar'):
                return 0
            
            try:
                return int(values['id'])
            except ValueError:
                sg.popup_error("ERRO: ID inválido.")


    '''def mostra_opcoes(self):
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
            return None'''
