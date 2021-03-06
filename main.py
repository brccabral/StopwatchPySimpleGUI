import PySimpleGUI as sg
import time


def create_window():
    sg.theme("black")
    layout = [
        [sg.Push(), sg.Image("cross.png", pad=0, enable_events=True, key="-CLOSE-")],
        [sg.VPush()],
        [sg.Text("0.0", key="-TIME-", font="Young 50")],
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
                visible=False,
            ),
        ],
        [sg.Column([[]], key="-LAPS-")],
        [sg.VPush()],
    ]

    return sg.Window(
        "Stowatch",
        layout,
        size=(300, 300),
        no_titlebar=True,
        element_justification="center",
        location=(100, 100),
    )


window = create_window()

start_time = 0
active = False
lap_number = 1
while True:
    # without timeout read() blokcs the code until an event happens
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, "-CLOSE-"):
        break

    if event == "-STARTSTOP-":
        if active:
            # from active to stop
            active = False
            window["-STARTSTOP-"].update("Reset")
            window["-LAP-"].update(visible=False)
        else:
            # from stop to reset
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_number = 1
            else:
                # from start to active
                start_time = time.time()
                active = True
                window["-STARTSTOP-"].update("Stop")
                window["-LAP-"].update(visible=True)

    if active:
        elapsed_time = round(time.time() - start_time, 1)
        window["-TIME-"].update(elapsed_time)

    if event == "-LAP-":
        elapsed_time = round(time.time() - start_time, 1)
        layout = [[sg.Text(f"{lap_number} | {elapsed_time}")]]
        window.extend_layout(window["-LAPS-"], layout)
        lap_number += 1

window.close()
