import PySimpleGUI as sg

layout = [
    [sg.Text('Breakfast', size=(15, 1), background_color="black" ), sg.InputText()],
    [sg.Text('lunch', size=(15, 1), background_color="black" ), sg.InputText()],
    [sg.Text('Dinner', size=(15, 1), background_color="black" ), sg.InputText()],

    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Food Directory', layout, background_color="yellow")
event, values = window.Read()
window.Close()

if event == 'Submit':
    # create before next GUI because I want to use the same name for variable `values`
    all_values = values.values() # values from dictionary
    text = "\n".join(all_values) # put values in separated lines

    layout = [
        [sg.Text('Filename', size=(15, 1), background_color="black" ), sg.InputText()],

        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Save file', layout, background_color="red")
    event, values = window.Read()
    window.Close()

    if event == 'Submit':
        name_file = values[0]+'.txt'

        try:
            fh = open(name_file, 'r+')
        except FileNotFoundError:
            fh = open(name_file, 'w+')

        fh.write(text) # write all as one string

        fh.close()

