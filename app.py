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
        window[f"Button-Profile"].update(disabled=True)
        window[f"Top-Profile"].update(visible=True)
        window[f"Content-Profile"].update(visible=True)
        window[f"Button-Experience"].update(disabled=False)
        window[f"Top-Experience"].update(visible=False)
        window[f"Content-Experience"].update(visible=False)
    if event == "Button-Experience":
        window[f"Button-Profile"].update(disabled=False)
        window[f"Top-Profile"].update(visible=False)
        window[f"Content-Profile"].update(visible=False)
        window[f"Button-Experience"].update(disabled=True)
        window[f"Top-Experience"].update(visible=True)
        window[f"Content-Experience"].update(visible=True)
    if event == "Button-Save-Profile":
        window[f"Button-Experience"].update(disabled=False)
        window[f"Button-Education"].update(disabled=False)
        window[f"Button-Hobbies"].update(disabled=False)
        window[f"Button-Skills"].update(disabled=False)
    if event == "Button-Delete-Profile" or event == "Button-New-Profile":
        window[f"Button-Profile"].update(disabled=True)
        window[f"Button-Experience"].update(disabled=True)
        window[f"Button-Education"].update(disabled=True)
        window[f"Button-Hobbies"].update(disabled=True)
        window[f"Button-Skills"].update(disabled=True)
        window[f"Button-Jobs"].update(disabled=True)
        window[f"Button-Interviews"].update(disabled=True)
# Close the window
window.close()
