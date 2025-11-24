import FreeSimpleGUI as sg

class PassagemTela:
    def __init__(self):
        self.__window = None

    def mostra_opcoes(self) -> int:
        layout = [
            [sg.Text('------ GERENCIAMENTO ------', font=('Helvetica', 12, 'bold'), justification='center', expand_x=True)],
            [sg.Text('Passagens', font=('Helvetica', 10, 'bold'))],
            [sg.Button('Emitir Passagem', key='1', size=(15,1)), sg.Button('Alterar Passagem', key='2', size=(15,1))],
            [sg.Button('Listar Passagens', key='3', size=(15,1)), sg.Button('Excluir Passagem', key='4', size=(15,1))],
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
        sg.Popup('Aviso', msg)

    def seleciona_pessoa_por_cpf(self) -> str:
        layout = [
            [sg.Text('------ SELECIONAR PASSAGEIRO --------', font=("Helvetica", 15))],
            [sg.Text('Digite o CPF do passageiro:', font=("Helvetica", 12))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Passageiro', layout)

        button, values = self.__window.read()
        
        if button in (None, 'Cancelar'):
            self.close()
            return ""

        cpf = values['cpf']
        self.close()
        return cpf

    def seleciona_transporte_por_id(self) -> int:
        layout = [
            [sg.Text('------ SELECIONAR TRANSPORTE --------', font=("Helvetica", 15))],
            [sg.Text('Digite o ID (índice) do transporte:', font=("Helvetica", 12))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Transporte', layout)

        button, values = self.__window.read()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        try:
            id_transporte = int(values['id'])
        except ValueError:
            self.close()
            return None

        self.close()
        return id_transporte

    def seleciona_cidade(self, tipo: str) -> str:
        layout = [
            [sg.Text(f'------ SELECIONAR {tipo.upper()} --------', font=("Helvetica", 15))],
            [sg.Text(f'Digite o nome da cidade de {tipo}:', font=("Helvetica", 12))],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Cidade', layout)

        button, values = self.__window.read()
        
        if button in (None, 'Cancelar'):
            self.close()
            return ""

        cidade = values['cidade']
        self.close()
        return cidade

    def pega_valor_passagem(self) -> float:
        layout = [
            [sg.Text('------ VALOR DA PASSAGEM --------', font=("Helvetica", 15))],
            [sg.Text('Digite o valor (ex: 250.75):', font=("Helvetica", 12))],
            [sg.Text('Valor R$:', size=(15, 1)), sg.InputText('', key='valor')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Valor Passagem', layout)

        button, values = self.__window.read()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        try:
            valor = float(values['valor'])
        except ValueError:
            self.close()
            return None

        self.close()
        return valor

    def mostra_passagem(self, dados: dict):
        string_passagem = f"--- PASSAGEM ID: {dados['id']} ---\n"
        string_passagem += f"Passageiro: {dados['passageiro']} (CPF: {dados['cpf']})\n"
        string_passagem += f"Rota: {dados['origem']} -> {dados['destino']}\n"
        string_passagem += f"Transporte: {dados['transporte']}\n"
        string_passagem += f"Valor: R$ {dados['valor']:.2f}\n"
        
        sg.Popup('Detalhes da Passagem', string_passagem)

    def pega_dados_para_alterar(self, dados_atuais: dict) -> dict:
        layout = [
            [sg.Text('-------- ALTERAR PASSAGEM ----------', font=("Helvetica", 15))],
            [sg.Text('Edite os campos (ou mantenha para não alterar):')],
            
            [sg.Text('CPF:', size=(15, 1)), 
             sg.InputText(default_text=dados_atuais['cpf'], key='cpf')],
            
            [sg.Text('ID Transporte:', size=(15, 1)), 
             sg.InputText(default_text=str(dados_atuais['id_transporte']), key='id_transporte')],
            
            [sg.Text('Origem:', size=(15, 1)), 
             sg.InputText(default_text=dados_atuais['origem'], key='origem')],
            
            [sg.Text('Destino:', size=(15, 1)), 
             sg.InputText(default_text=dados_atuais['destino'], key='destino')],
            
            [sg.Text('Valor:', size=(15, 1)), 
             sg.InputText(default_text=str(dados_atuais['valor']), key='valor')],
             
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        
        self.__window = sg.Window('Alterar Passagem', layout)
        button, values = self.__window.read()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None
        
        novo_cpf = values['cpf']
        novo_id_transporte = values['id_transporte']
        nova_origem = values['origem']
        nova_destino = values['destino']
        novo_valor = values['valor']
        
        self.close()

        try:
            return {
                "cpf": novo_cpf or dados_atuais['cpf'],
                "id_transporte": int(novo_id_transporte) if novo_id_transporte else dados_atuais['id_transporte'],
                "origem": nova_origem or dados_atuais['origem'],
                "destino": nova_destino or dados_atuais['destino'],
                "valor": float(novo_valor) if novo_valor else dados_atuais['valor'],
            }
        except:
            return None

    def seleciona_passagem_por_id(self) -> int:
        layout = [
            [sg.Text('------ SELECIONAR PASSAGEM --------', font=("Helvetica", 15))],
            [sg.Text('Digite o ID da passagem:', font=("Helvetica", 12))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Passagem', layout)

        button, values = self.__window.read()
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        try:
            id_passagem = int(values['id'])
        except ValueError:
            self.close()
            return None

        self.close()
        return id_passagem

    def close(self):
        if self.__window:
            self.__window.Close()
            self.__window = None
