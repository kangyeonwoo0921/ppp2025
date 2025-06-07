import PySimpleGUI as sg
layout = [
    [sg.Text("What's your name?")],
    [sg.InputText(key='-INPUT-')],
    [sg.Text('', size=(30,1), key='-OUTPUT-')],
    [sg.Button('Ok'), sg.Button('Cancel')]
]
# Create the Window
window = sg.Window('Hello Example', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
if event == 'Ok':
    value_dollar = float(values['-INPUT-']).sg.Button('OK'),
    name = values['-INPUT-']
    # print('Hello', name, '!')
    window['-OUTPUT-'].update(f"value_dollar * 1367")
window.close()