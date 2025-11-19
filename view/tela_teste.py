import FreeSimpleGUI as sg

layout = [
    [sg.Text('Incluir novo Cliente')],
    [sg.Text('Nome', size =(15, 1)), sg.InputText(key = 'nome')],
    [sg.Text('Idade', size = (15, 1)), sg.InputText(key = 'idade')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Cadastro de Clientes').Layout(layout)

button, values = window.Read()

print(button, type(values))

'''layout = [
    [sg.Text("Teste opções")],
    [sg.Button("button 1", key="button1")],
    [sg.Button("button 2", key="button3")]
]

window = sg.Window("Teste", layout=layout)

def button1():
    sg.Popup("button1 was clicked")


while True:
    event, values = window.Read()

    if event == sg.WIN_CLOSED:
        break
    if event == "button1":
        button1()

window.close()'''