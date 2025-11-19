import FreeSimpleGUI as sg

class CidadeTela:
    def __init__(self):
        self.__window = None

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.__window.read()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['8']:
            opcao = 8
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0

        self.close()
        return opcao    
    
    def init_opcoes(self):
    #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('----- PASSEIO TURÍSTICO ------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Text('---PAÍS---', font=("Helvica", 15))],
            [sg.Radio('Cadastrar País', "RD1", key='1')],
            [sg.Radio('Alterar País', "RD1", key='2')],
            [sg.Radio('Listar Países', "RD1", key='3')],
            [sg.Radio('Excluir País', "RD1", key='4')],
            [sg.Text('---CIDADE---', font=("Helvica", 15))],
            [sg.Radio('Cadastrar Cidade', "RD1", key='5')],
            [sg.Radio('Alterar Cidade', "RD1", key='6')],
            [sg.Radio('Listar Cidades', "RD1", key='7')],
            [sg.Radio('Excluir Cidade', "RD1", key='8')],
            [sg.Text('---SISTEMA---', font=("Helvica", 15))],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Controlador de viagens').Layout(layout)

    def pega_dados_pais(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS PAÍS ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controlador viagens').Layout(layout)

        button, values = self.__window.read()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        nome = values['nome']

        self.close()
        return {"nome": nome}
    
    def mostra_pais(self, dados_pais):
        layout = [
            [sg.Text('------------------')],
            [sg.Text(f"ID: {dados_pais['id']}")],
            [sg.Text(f"NOME: {dados_pais['nome']}")],
            [sg.Button('OK')]
        ]
        
        window = sg.Window('Detalhes do Passeio', layout)



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