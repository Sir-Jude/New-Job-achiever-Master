# Import all layouts elements
from layout import sg, menu
from layout import (
    top_profile,
    top_experience,
)  # , top_education, top_hobbies, top_skills
from layout import (
    content_profile,
    content_experience,
)  # , content_education, content_hobbies, content_skills

# Defining the layout for entire interface
layout = [
    [sg.Frame(layout=[[top_profile, top_experience]], title="", expand_x=True)],
    [
        sg.Frame(
            layout=[[menu, content_profile, content_experience]],
            title="",
            expand_x=True,
        )
    ],
]

# Create the window
window = sg.Window("Job Achiever Master", layout)

# Events loop starting
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # Process the elements here
    if event == "Button-Profile":
        window["Button-Profile"].update(disabled=True)
        window["Top-Profile"].update(visible=True)
        window["Content-Profile"].update(visible=True)
        window["Button-Experience"].update(disabled=False)
        window["Top-Experience"].update(visible=False)
        window["Content-Experience"].update(visible=False)
    if event == "Button-Experience":
        window["Button-Profile"].update(disabled=False)
        window["Top-Profile"].update(visible=False)
        window["Content-Profile"].update(visible=False)
        window["Button-Experience"].update(disabled=True)
        window["Top-Experience"].update(visible=True)
        window["Content-Experience"].update(visible=True)
    if event == "Button-Save-Profile":
        window["Button-Experience"].update(disabled=False)
        window["Button-Education"].update(disabled=False)
        window["Button-Hobbies"].update(disabled=False)
        window["Button-Skills"].update(disabled=False)
    if event == "Button-Delete-Profile" or event == "Button-New-Profile":
        window["Button-Profile"].update(disabled=True)
        window["Button-Experience"].update(disabled=True)
        window["Button-Education"].update(disabled=True)
        window["Button-Hobbies"].update(disabled=True)
        window["Button-Skills"].update(disabled=True)
        window["Button-Jobs"].update(disabled=True)
        window["Button-Interviews"].update(disabled=True)
        window["Combo-Profiles"].update(values=['Blabla 1','Blaba 2'])
# Close the window
window.close()
