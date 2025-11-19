import FreeSimpleGUI as sg

class SistemaTela:
    def __init__(self):
        self.__window = None
        self.init_components()

    def tela_opcoes(self):
        self.init_components()
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
        
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao controlador de viagens', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Pessoa',"RD1", key='1')],
            [sg.Radio('Grupo',"RD1", key='2')],
            [sg.Radio('Cidade/País',"RD1", key='3')],
            [sg.Radio('Passeio Turístico',"RD1", key='4')],
            [sg.Radio('Transporte',"RD1", key='5')],
            [sg.Radio('Pacote',"RD1", key='6')],
            [sg.Radio('Pagamento',"RD1", key='7')],
            [sg.Radio('Gerar relatório',"RD1", key='8')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Controlador viagens').Layout(layout)
        

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