import FreeSimpleGUI as sg

class PasseioTuristicoTela:
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
            [sg.Radio('Incluir Passeio', "RD1", key='1')],
            [sg.Radio('Alterar Passeio', "RD1", key='2')],
            [sg.Radio('Listar Passeios', "RD1", key='3')],
            [sg.Radio('Excluir Passeio', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
        self.__window = sg.Window('Controlador de viagens').Layout(layout)

    def pega_dados_passeio(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS PASSEIO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Preco:', size=(15, 1)), sg.InputText('', key='preco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controlador viagens').Layout(layout)

        button, values = self.__window.read()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        nome = values['nome']
        preco = values['preco']

        self.close()
        return {"nome": nome, "preco": preco}

    def mostra_lista_passeios(self, dados_passeios):
        string_todos_passeios = ""
        for dado in dados_passeios:
            string_todos_passeios += "ID: " + str(dado.id) + '\n'
            string_todos_passeios += "NOME: " + str(dado.nome) + '\n'
            string_todos_passeios += "PREÇO: " + str(dado.preco) + '\n\n'

        sg.Popup('-------- LISTA DE PASSEIOS ----------', string_todos_passeios)

    def seleciona_passeio_por_id(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('------ SELECIONAR POR ID --------', font=("Helvetica", 25))],
            [sg.Text('Digite o ID do passeio:', font=("Helvetica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Passeio', layout)

        button, values = self.__window.read()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        try:
            id_passeio = int(values['id'])
        except ValueError:
            sg.Popup("Erro", "O ID precisa ser um número inteiro.")
            self.close()
            return None

        self.close()
        return id_passeio
    
    def seleciona_passeio_por_nome(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('------ SELECIONAR PASSEIO NOME --------', font=("Helvica", 25))],
            [sg.Text('Digite o NOME do PASSEIO que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('NOME:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Passeio', layout)

        button, values = self.__window.read()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        nome = values['nome']
        self.close()
        return nome
        
    def close(self):
        if self.__window:
            self.__window.Close()
    
    def mostra_mensagem(self, msg: str):
        sg.Popup('Aviso', msg)
        
        '''print("\n===== PASSEIOS TURÍSTICOS =====")
        print("> (1) Incluir Passeio")
        print("> (2) Alterar Passeio")
        print("> (3) Listar Passeios")
        print("> (4) Excluir Passeio")
        print("--------------------------------")
        print("> (0) Retornar")
        print("================================")
        print()
        
        try:
            return int(input("Escolha uma opção: "))
        except:
            return None'''

    '''def mostra_mensagem(self, msg: str):
        print(msg)'''

    '''def pega_dados_passeio(self) -> dict:
        print("\n-- DADOS DO PASSEIO --")
        nome = input("Nome: ")
        preco = input("Preço (ex: 49.90): ")
        return {"nome": nome, "preco": preco}'''

    '''def mostra_passeio(self, dados: dict):
        print(f"  > ID: {dados['id']} | Nome: {dados['nome']} | Preço: R$ {dados['preco']:.2f}")'''
    
    '''def seleciona_passeio_por_nome(self) -> str:
        return input("Informe o nome do passeio que deseja selecionar: ")'''

    '''def seleciona_passeio_por_id(self) -> int:
        return int(input("Informe o ID do passeio que deseja selecionar: "))'''
