import FreeSimpleGUI as sg 
from akkadian_engine import Noun
from disambiguate import NounPhrase
import os 
sg.theme('SystemDefaultForReal')
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
IMAGE_PATH = os.path.join(BASE_DIR, "v2.png")
layout = [
    [sg.Image(filename=IMAGE_PATH, key="-IMAGE-")],
    [sg.Text('Enter noun here: '), sg.InputText(key='-INPUT-'), sg.Button('Analyze')],
    [sg.Text('Gender: ', key="-GENDER-"), sg.Text('Number: ',key='-NUMBER-'),sg.Text('Case:',key='-CASE-'),sg.Text('State:',key='-STATE-')],
    [sg.Text('Gender: ', key="-GENDER-2"), sg.Text('Number: ',key='-NUMBER-2'),sg.Text('Case:',key='-CASE-2'),sg.Text('State:',key='-STATE-2')]
    ]

window = sg.Window('Akkadian Nominal Morphoanalyzer V2.0', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Analyze':
        noun2 = None
        input_vals = values['-INPUT-'].strip()
        if " " in input_vals:
            val1, val2 = input_vals.split()
            noun = Noun(val1)
            noun2 = Noun(val2)
            np = NounPhrase(noun, noun2)
            np.disambiguate()
        else:
            noun = Noun(values['-INPUT-'].strip())

        window["-GENDER-"].update(f"Gender: {noun.gender}")
        window["-NUMBER-"].update(f"Number: {noun.number}")
        window["-CASE-"].update(f"Case: {noun.case}")
        window["-STATE-"].update(f"State: {noun.state}")
    if noun2 is not None:
        window["-GENDER-2"].update(f"Gender: {noun2.gender}")
        window["-NUMBER-2"].update(f"Number: {noun2.number}")
        window["-CASE-2"].update(f"Case: {noun2.case}")
        window["-STATE-2"].update(f"State: {noun2.state}")
    else:
        window["-GENDER-2"].update(f"Gender: None")
        window["-NUMBER-2"].update(f"Number: None")
        window["-CASE-2"].update(f"Case: None")
        window["-STATE-2"].update(f"State: None")
window.close()
