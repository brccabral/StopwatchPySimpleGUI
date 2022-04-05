import PySimpleGUI as sg

sg.theme("black")
layout = [
    [sg.Push(), sg.Image("cross.png", pad=0)],
    [sg.VPush()],
    [sg.Text("time", key="-TEXT-")],
    [
        sg.Button("Start", key="-BUTTON1-", expand_x=False),
        sg.Button("Lap", key="-BUTTON2-", expand_x=False),
    ],
    [sg.VPush()],
]

window = sg.Window(
    "Stowatch",
    layout,
    size=(300, 300),
    no_titlebar=True,
    element_justification="center",
    location=(100, 100),
)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "-BUTTON1-"):
        break

window.close()
