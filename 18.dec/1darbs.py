import PysimpleGUI as sg

#visus loga elementus apveino masīvā - vārdnīca

daljas=[
    [sg.Text('Uzrakstīts teksts 1.rindā!')],
    [sg.Text('Ievadi savu vārdu: ')],
    [sg.Button('OK'), sg.Button('cancel')]
]

# Tiek veidots logs 

mans_logs=sg.Window('***ZIEMA***,'daljas,size=(320,150), icon=bilde)


# Organizēt procesu - rādīt logu! EVENT, VALUES

while True:
    notikums, vertibas=mans_logs.read()



mans_logs.close()
