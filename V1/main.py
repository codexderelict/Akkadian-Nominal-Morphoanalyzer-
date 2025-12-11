import FreeSimpleGUI as sg 
from akkadian_engine import Noun
sg.theme('SystemDefaultForReal')
layout = [
    [sg.Text('Enter noun here: '), sg.InputText(key='-INPUT-'), sg.Button('Analyze')],
    [sg.Text('Gender: ', key="-GENDER-"), sg.Text('Number: ',key='-NUMBER-'),sg.Text('Case:',key='-CASE-')]

]
window = sg.Window('Nominal Akkadian Morphoanalyzer V1.0', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Analyze':
        noun = Noun(values['-INPUT-'].strip())
        window["-GENDER-"].update(f"Gender: {noun.gender}")
        window["-NUMBER-"].update(f"Number: {noun.number}")
        window["-CASE-"].update(f"Case: {noun.case}")
window.close()
        

    

