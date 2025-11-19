import FreeSimpleGUI as sg


class GrupoTela:
    def __init__(self):
        self.__window_menu = None

    def mostra_opcoes(self):
        '''print("====== OPÇÕES ======")
        print("> (1) Criar Grupo")
        print("> (2) Excluir Grupo")
        print("> (3) Incluir Membro")
        print("> (4) Remover Membro")
        print("> (5) Listar Membros do Grupo")
        print("> (0) Retonar")
        print("=====================")
        print()

        opcao = input("Escolha uma opção: ")

        #Tenta converter o input em inteiro. Se falhar retorna None
        try:
            opcao = int(opcao)
            return opcao
        except:
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("OPÇÕES DE GRUPO"), sg.Push()],
            [sg.Button("Criar Grupo", key=1)],
            [sg.Button("Excluir Grupo", key=2)],
            [sg.Button("Incluir Membro", key=3)],
            [sg.Button("Remover Membro", key=4)],
            [sg.Button("Listar Membros do Grupo", key=5)],
            [sg.Cancel("Retornar", key=0)]
        ]

        if self.__window_menu is None:
            self.__window_menu = sg.Window("OPÇÕES DE GRUPO", layout=layout, size=(400, 300))

        while True:
            event, values = self.__window_menu.read()

            if event == 0 or event == sg.WIN_CLOSED:
                self.__window_menu.close()
                self.__window_menu = None
            
            return event
        
    def pegar_codigo_grupo(self):
        '''codigo = input("> Código do Grupo: ")

        try:
            codigo = int(codigo)
            return codigo
        except:
            return None'''
        
        layout = [
            [sg.Push(), sg.Text("CÓDIGO DO GRUPO"), sg.Push()],
            [sg.Text("Código do Grupo"), sg.InputText(key="codigo")],
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
            [sg.Text("Código do Grupo"), sg.InputText(key="codigo")],
            [sg.Text("CPF do Usuário"), sg.InputText(key="cpf")],
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
        '''print("=======================================")
        print(f"> Nome: {membro_dict['nome']}")
        print(f"> CPF: {membro_dict['cpf']}")
        print(f"> Data de Nascimento: {membro_dict['data_nascimento']}")
        print(f"> Telefone: {membro_dict['telefone']}")
        print("=======================================")'''

        string_membros = ''

        for membro in dados_membros:
            string_membros += f"Nome: {membro["nome"]}\n"
            string_membros += f"CPF: {membro["cpf"]}\n"
            string_membros += f"Data de Nascimento: {membro["data_nascimento"]}\n"
            string_membros += f"Telefone: {membro["telefone"]}\n\n"

        sg.Popup("LISTA DE MEMBROS DO GRUPO\n", string_membros, non_blocking = True)

    def mostrar_grupos(self, dados_grupos: list):

        string_grupos = ""

        for grupo in dados_grupos:
            string_grupos += f"Grupo {grupo["codigo"]}\n"

        sg.Popup("LISTA DE GRUPOS\n", string_grupos, non_blocking = True)

    def mostrar_mensagem(self, msg):
        sg.Popup(msg)
