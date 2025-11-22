import FreeSimpleGUI as sg

class SistemaTela:
    def __init__(self):
        self.__window = None
        sg.set_options(
            font=("Helvetica", 10, "bold"), 
            )
        sg.theme("SandyBeach")
    
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
    
    def gerar_relatorio(self, dados):
        '''print("======= RELATÓRIO =======")
        print(f"> Número de pessoas: {dados["pessoas"]}")
        print(f"> Número de grupos: {dados["grupos"]}")
        print(f"> Cidade mais visitada: {dados["cidade_mais_visitada"]} ({dados["cidade_quant_visitas"]})")
        print(f"> Passeio mais barato: {dados["passeio_mais_barato"]} ({dados["preco_barato"]})")
        print(f"> Passeio mais caro: {dados["passeio_mais_caro"]} ({dados["preco_caro"]})")'''

        layout = [
            [sg.Text("------ RELATÓRIO ------", justification="c", expand_x=True, font=("Helvetica", 12, "bold"))],
            [sg.Text(f"Número de pessoas cadastradas: {dados["pessoas"]}")],
            [sg.Text(f"Número de grupos cadastrados: {dados["grupos"]}")],
            [sg.Text(f"Cidade mais visitada: {dados["cidade_mais_visitada"]} ({dados["cidade_quant_visitas"]} visitas)")],
            [sg.Text(f"Passeio mais barato: {dados["passeio_mais_barato"]} ({dados["preco_barato"]})")],
            [sg.Text(f"Passeio mais caro: {dados["passeio_mais_caro"]} ({dados["preco_caro"]})")],
            [sg.Push(), sg.Cancel("Retornar", key=0, button_color=("white", "firebrick3"), size=(15, 1)), sg.Push()]
        ]

        window = sg.Window("Relatório", layout=layout)

        while True:
            event, values = window.read()

            if event == 0 or event == sg.WIN_CLOSED:
                window.close()
                break

    def mostrar_mensagem(self, msg):
        sg.popup(msg)

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

