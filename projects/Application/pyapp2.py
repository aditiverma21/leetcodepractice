import PySimpleGUI as sg
layout = [[sg.Text("Hello from PySimpleGUI")],[sg.Button("OK")]]

#Create the Window

window = sg.Window(title="Demo", layout=layout, margins=(300,150))

# Create an event loop
while True:
    event, values = window.read()

    if event== "OK" or event== sg.WIN_CLOSED:
        break

window.close()