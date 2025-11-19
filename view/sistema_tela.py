import FreeSimpleGUI as sg

class SistemaTela:
    def __init__(self):
        self.__window = None
    
    def mostra_opcoes(self) -> int:
        layout = [
            [sg.Text('------ SISTEMA ------', font=('Helvetica', 12, 'bold'), justification='center', expand_x=True)],
            [sg.Text('--INDÍVIDUOS--', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Pessoa', key='1', size=(15,1)), sg.Button('Grupo', key='2', size=(15,1))],
            [sg.Text('--LOCAIS--', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Cidade/País', key='3', size=(15,1)), sg.Button('Passeio Turístico', key='4', size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Text('--PLANO--', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Transporte', key='5', size=(15,1)), sg.Button('Pacote', key='6', size=(15,1))],
            [sg.Text('--FINANCEIRO--', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Pagamento', key='7', size=(15,1)), sg.Button('Gerar relatório', key='8', size=(15,1))],
            [sg.HorizontalSeparator()],
            [sg.Button('Sair', key='0', button_color=('white', 'firebrick3'), size=(32,1))]
        ]

        window = sg.Window('Menu Principal', layout, element_justification='c')

        event, values = window.read()
        window.close()

        if event in (sg.WIN_CLOSED, '0'):
            return 0

        return int(event)
        

if __name__ == "__main__":
    tela = SistemaTela()
    opcao_escolhida = tela.tela_opcoes()
    print(f"Você escolheu a opção: {opcao_escolhida}")
    
    '''def opcoes(self):
        print("====== OPÇÕES ======")
        print("> (1) PESSOA")
        print("> (2) GRUPO")
        print("> (3) CIDADE/PAÍS")
        print("> (4) PASSEIO TURÍSTICO")
        print("> (5) TRANSPORTE")
        print("> (6) PACOTE")
        print("> (7) PAGAMENTO")
        print("> (8) GERAR RELATÓRIO")
        print("> (0) SAIR")
        print("=====================")
        print()
        
        opcao = input("Escolha uma opção: ")
        
        try:
            opcao = int(opcao)
            return opcao
        except:
            return None'''
        
    '''def gerar_relatorio(self, dados):
        print("======= RELATÓRIO =======")
        print(f"> Número de pessoas: {dados["pessoas"]}")
        print(f"> Número de grupos: {dados["grupos"]}")
        print(f"> Número de cidades: {dados["cidades"]}")
        print(f"> Número de países: {dados["paises"]}")
        print(f"> Número de passeios turísticos: {dados["passeios_turisticos"]}")
        print("=========================")'''

    def mostrar_mensagem(self, msg):
        print(msg)
