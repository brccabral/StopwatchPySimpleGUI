import PySimpleGUI as sg
import time

sg.theme("black")
layout = [
    [sg.Push(), sg.Image("cross.png", pad=0, enable_events=True, key="-CLOSE-")],
    [sg.VPush()],
    [sg.Text("time", key="-TIME-", font="Young 50")],
    [
        sg.Button(
            "Start",
            key="-STARTSTOP-",
            expand_x=False,
            button_color=("#FFFFFF", "#FF0000"),
            border_width=0,
        ),
        sg.Button(
            "Lap",
            key="-LAP-",
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

start_time = 0
active = False
while True:
    # without timeout read() blokcs the code until an event happens
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, "-CLOSE-"):
        break

    if event == "-STARTSTOP-":
        start_time = time.time()
        active = True

    if active:
        elapsed_time = round(time.time() - start_time, 1)
        window["-TIME-"].update(elapsed_time)

window.close()
