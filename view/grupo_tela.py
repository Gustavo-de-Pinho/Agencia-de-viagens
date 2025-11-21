import FreeSimpleGUI as sg


class GrupoTela:
    def __init__(self):
        self.__window_menu = None

    def mostra_opcoes(self):
        
        layout = [
            [sg.Text("------ GERENCIAMENTO ------", font=("Helvetica", 12, "bold"), justification="center", expand_x=True)],
            [sg.Push(), sg.Text("Grupo"), sg.Push()],
            [sg.Button("Criar Grupo", key=1, size=(15, 1)), sg.Button("Excluir Grupo", key=2, size=(15, 1))],
            [sg.Button("Incluir Membro", key=3, size=(15, 1)), sg.Button("Remover Membro", key=4, size=(15, 1))],
            [sg.Button("Listar Membros", key=5, size=(15, 1)), sg.Cancel("Retornar", key=0, button_color=("white", "firebrick3"), size=(15, 1))]
        ]

        if self.__window_menu is None:
            self.__window_menu = sg.Window("OPÇÕES DE GRUPO", layout=layout)

        while True:
            event, values = self.__window_menu.read()

            if event == 0 or event == sg.WIN_CLOSED:
                self.__window_menu.close()
                self.__window_menu = None
                return 0
            
            return event
        
    def pegar_codigo_grupo(self):
        
        layout = [
            [sg.Push(), sg.Text("CÓDIGO DO GRUPO"), sg.Push()],
            [sg.Text("Código do Grupo"), sg.Push(), sg.InputText(key="codigo", size=(32, 1))],
            [sg.Submit()]
        ]

        window = sg.Window("Grupo", layout=layout)

        botao, dados_dict = window.Read()
        window.close()

        try:
            codigo = int(dados_dict["codigo"])
            return codigo
        except:
            return None

    def pegar_codigo_e_cpf(self):
        
        layout = [
            [sg.Text("------ CÓDIGO E CPF ------", justification="c", expand_x=True)],
            [sg.Text("Código do Grupo"), sg.Push(), sg.InputText(key="codigo", size=(32, 1))],
            [sg.Text("CPF do Usuário"), sg.Push(), sg.InputText(key="cpf", size=(32, 1))],
            [sg.Submit()]
        ]

        window = sg.Window("Grupo", layout=layout)
        
        botao, dados_dict = window.Read()
        window.close()

        try:
            dados_dict["codigo"] = int(dados_dict["codigo"])
            return dados_dict
        except:
            return None

    def criar_grupo(self):
        codigo = self.pegar_codigo_grupo()

        return codigo
        
    def excluir_grupo(self):
        codigo = self.pegar_codigo_grupo()

        return codigo

    def adicionar_membro(self):
        dados_dict = self.pegar_codigo_e_cpf()

        return dados_dict
        
    def remover_membro(self):
        dados_dict = self.pegar_codigo_e_cpf()

        return dados_dict
        
    def listar_membros(self):
        codigo = self.pegar_codigo_grupo()

        if codigo is not None:
            return codigo
        else:
            return None
        
    def mostrar_membros(self, dados_membros: list):

        string_membros = ''

        for membro in dados_membros:
            string_membros += f"Nome: {membro["nome"]}\n"
            string_membros += f"CPF: {membro["cpf"]}\n"
            string_membros += f"Data de Nascimento: {membro["data_nascimento"]}\n"
            string_membros += f"Telefone: {membro["telefone"]}\n\n"

        sg.Popup("------ LISTA DE MEMBROS DO GRUPO ------\n", string_membros, non_blocking = True)

    def mostrar_grupos(self, dados_grupos: list):

        string_grupos = ""

        for grupo in dados_grupos:
            string_grupos += f"Grupo {grupo["codigo"]}\n"

        sg.Popup("------ LISTA DE GRUPOS ------\n", string_grupos, non_blocking = True)

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
