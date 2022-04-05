import PySimpleGUI as sg

sg.theme("black")
layout = [
    [sg.Push(), sg.Image("cross.png", pad=0, enable_events=True, key="-CLOSE-")],
    [sg.VPush()],
    [sg.Text("time", key="-TEXT-", font="Young 50")],
    [
        sg.Button(
            "Start",
            key="-BUTTON1-",
            expand_x=False,
            button_color=("#FFFFFF", "#FF0000"),
            border_width=0,
        ),
        sg.Button(
            "Lap",
            key="-BUTTON2-",
            expand_x=False,
            button_color=("#FFFFFF", "#FF0000"),
            border_width=0,
        ),
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
    if event in (sg.WIN_CLOSED, "-CLOSE-"):
        break

window.close()
