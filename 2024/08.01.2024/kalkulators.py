import PySimpleGUI as sg
# Iestatīt tēmu (vizuālo izskatu)
sg.theme('LightGreen2') # Reddit  Dark2 Green Tan
 
# Attēls pie loga nosaukuma ===*.ico
bilde='aka.ico'
 
# Iekšējā funkcija, kas veic aprēķinus
def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operation == '+':
            result = num1 + num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '-':
            result=num1-num2
        else:
            result = None
        return result
    except ValueError:
        return "Kļūda"
 
# Palīgmaine, lai uzglabātu ievades datus
current_input = ''
current_operation = ''
 
# Izveidojiet GUI loga izkārtojumu
layout = [
    [sg.InputText(key='-DISPLAY-', size=(20, 1), justification='right', readonly=True)],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('+'), sg.Button('-')],
    [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
    [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('C')],
    [sg.Button('0'), sg.Button('='), sg.Button('Exit', key='-EXIT-')],
]
 
# Izveidojiet logu ar iepriekš definēto izkārtojumu
window = sg.Window('Kalkulators', layout, resizable=True, icon=bilde)
 
# Balstoties uz notikumu ciklu
while True:
    event, values = window.read()
 
    # Ja loga aizvēršanas notikums vai Exit poga tiek nospiesta, tad iziet no cikla
    if event == sg.WIN_CLOSED or event == '-EXIT-':
        break
 
    # Ja skaitļu poga tiek nospiesta, pievieno to skaitļu teksta ievades laukam
    elif event in '1234567890':
        current_input += event
        window['-DISPLAY-'].update(current_input)
 
    # Ja darbības poga tiek nospiesta, saglabā šo darbību un notīra teksta ievades lauku
    elif event in ['+', '*', '-']:
        current_operation = event
        current_input = ''
        window['-DISPLAY-'].update(current_input)
 
    # Ja "C" poga tiek nospiesta, notīra teksta ievades lauku un darbību
    elif event == 'C':
        current_input = ''
        current_operation = ''
        window['-DISPLAY-'].update(current_input)
 
    # Ja "=" poga tiek nospiesta, veic kalkulācijas un atjauno teksta ievades lauku ar rezultātu
    elif event == '=':
        result = calculate(current_input, values['-DISPLAY-'], current_operation)
        window['-DISPLAY-'].update(result if result is not None else '')
        current_input = str(result) if result is not None else ''
 
# Aizveriet GUI logu
window.close()
