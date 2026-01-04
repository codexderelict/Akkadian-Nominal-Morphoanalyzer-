import FreeSimpleGUI as sg 
from akkadian_engine import Noun
sg.theme('SystemDefaultForReal')
layout = [
    [sg.Image(filename='v11.png', key="-IMAGE-")],
    [sg.Text('Enter noun here: '), sg.InputText(key='-INPUT-'), sg.Button('Analyze')],
    [sg.Text('Gender: ', key="-GENDER-"), sg.Text('Number: ',key='-NUMBER-'),sg.Text('Case:',key='-CASE-'),sg.Text('State:',key='-STATE-')]

]
window = sg.Window('Akkadian Nominal Morphoanalyzer V1.1', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Analyze':
        noun = Noun(values['-INPUT-'].strip())
        window["-GENDER-"].update(f"Gender: {noun.gender}")
        window["-NUMBER-"].update(f"Number: {noun.number}")
        window["-CASE-"].update(f"Case: {noun.case}")
        window["-STATE-"].update(f"State: {noun.state}")
window.close()
        

    


