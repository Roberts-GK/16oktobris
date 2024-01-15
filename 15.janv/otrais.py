#Pielagoti logriki ar PySimpleGUI

import PySimpleGUI as sg

layout=[
    [sg.Text('Ievadi savu vārdu:'),sg.InputText(key='-IN-', enable_events=True) ],
    [sg.Text('Ievadi savu vārdu:'),sg.InputText(key='-INN-', enable_events=True) ],
    [sg.Button('OK')],
    [sg.Text('',key='-OUTPUT-' )]

]
window=sg.Window('Ziema',layout)
while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED:
        break
        # pārbaudīt vai ir ievadīti vārds un uzvārds
    elif event=='OK':
        if values['-IN-'] and values['-INN-']:
            # attēlojam ievadīto informāciju tukšajā teksta laukā...
            window['-OUTPUT-'].update(f" Mani sauc {values['-IN-']} {values['-INN-']}.")
        else:
            sg.popup_error('Lūdzu, ievadiet vārdu un uzvārdu.')
   
"""  
    if event=='OK':
        print(f" Mani sauc {values['-IN-']} {values['-INN-']}.") #izdrukā ievadīto info terminālī
"""



window.close()