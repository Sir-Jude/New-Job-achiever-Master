# Import all layouts elements
from layout import sg, menu
from layout import top_profile, top_experience#, top_education, top_hobbies, top_skills
from layout import content_profile, content_experience#, content_education, content_hobbies, content_skills

# Defining the layout for entire interface
layout = [
    [sg.Frame(layout=[[top_profile, top_experience]], title="", expand_x=True)],
    [sg.Frame(layout=[[menu, content_profile, content_experience]], title="", expand_x=True)],
]

# Create the window
window = sg.Window("Job Achiever Master", layout)

# Events loop starting
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    # Process the elements here
    if event == "-PROFILE-":
        window[f'-Profile-'].update(visible=False)
        window[f'-Experience-'].update(visible=True)
        window[f'-TopProfile-'].update(visible=False)
        window[f'-TopExperience-'].update(visible=True)
        window[f'-PROFILE-'].update(disabled=True)
        window[f'-EXPERIENCE-'].update(disabled=False)
    if event == "-EXPERIENCE-":
        window[f'-Profile-'].update(visible=True)
        window[f'-Experience-'].update(visible=False)
        window[f'-TopProfile-'].update(visible=True)
        window[f'-TopExperience-'].update(visible=False)
        window[f'-PROFILE-'].update(disabled=False)
        window[f'-EXPERIENCE-'].update(disabled=True)

# Close the window
window.close()
