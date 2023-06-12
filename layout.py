import PySimpleGUI as sg

sg.theme("LightGrey2")

# Defining the left menu
menu = sg.vtop(
    sg.Column(
        layout=[
            [
                sg.Button(
                    button_text="Profile", expand_x=True, disabled=True, key="-PROFILE-"
                )
            ],
            [sg.Button(button_text="Experience", expand_x=True, key="-EXPERIENCE-")],
            [sg.Button(button_text="Education", expand_x=True, key="-EDUCATION-")],
            [sg.Button(button_text="Hobbies", expand_x=True, key="-HOBBIES-")],
            [sg.Button(button_text="Skills", expand_x=True, key="-SKILLS-")],
            [sg.Button(button_text="Jobs", expand_x=True, key="-JOBS-")],
            [sg.Button(button_text="Interviews", expand_x=True, key="-INTERVIEWS-")],
        ],
        element_justification="left",
    )
)

# PROFILE LAYOUT
# Defining the options for profiles combo box
profiles = ["Adrian George Radu", "Profile 2", "Profile 3"]
# Defining the top frame
top_profile = sg.Column(
    [
        [
            sg.Column(
                [
                    [
                        sg.Image(filename="images/icons8-document-writer-50.png"),
                    ]
                ],
                element_justification="left",
            ),
            sg.Column(
                [
                    [
                        sg.Text("Select Profile:"),
                        sg.Combo(profiles, key="-Profiles-", readonly=True),
                        sg.Button("New Profile"),
                        sg.Button("Delete profile"),
                    ]
                ],
                element_justification="right",
                expand_x=True,
            ),
        ],
    ],
    key="-TopProfile-",
    visible=True,
)
# Defining the content
content_profile = sg.Column(
    [
        [sg.Text("Name:"), sg.Input(key="-Name-")],
        [sg.Text("Surname:"), sg.Input(key="-Surname-")],
        [sg.Text("Birthday:"), sg.Input(key="-Birthday-")],
        [sg.Text("Sex:"), sg.Input(key="-Sex-")],
        [sg.Text("Phone:"), sg.Input(key="-Phone-")],
        [sg.Text("E-mail:"), sg.Input(key="-Email-")],
        [sg.Text("E-mail pass:"), sg.Input(key="-EmailPass-")],
        [sg.Text("Address:"), sg.Input(key="-Address-")],
        [sg.Text("Language:"), sg.Input(key="-Language-")],
        [sg.Text("Photo:"), sg.Input(size=(33, 1), key="-FILE-"), sg.FileBrowse()],
        [sg.Button("Save")],
    ],
    element_justification="right",
    expand_x=True,
    key="-Profile-",
    visible=True,
)

# EXPERIENCE LAYOUT
# Defining the top frame
top_experience = sg.Column(
    [
        [
            sg.Column(
                [
                    [
                        sg.Image(filename="images/icons8-populärer-mann-50.png"),
                    ]
                ],
                element_justification="left",
            ),
            sg.Column(
                [[sg.Text("Experience of Adrian George Radu")]],
                element_justification="right",
                expand_x=True,
            ),
        ],
    ],
    key="-TopExperience-",
    visible=False,
)

# Defining the content
content_experience = sg.Column(
    [
        [sg.Text("Nameeeee:"), sg.Input(key="-Name-")],
        [sg.Text("Surname:"), sg.Input(key="-Surname-")],
        [sg.Text("Birthday:"), sg.Input(key="-Birthday-")],
        [sg.Text("Sex:"), sg.Input(key="-Sex-")],
        [sg.Text("Phone:"), sg.Input(key="-Phone-")],
        [sg.Text("E-mail:"), sg.Input(key="-Email-")],
        [sg.Text("E-mail pass:"), sg.Input(key="-EmailPass-")],
        [sg.Text("Address:"), sg.Input(key="-Address-")],
        [sg.Text("Language:"), sg.Input(key="-Language-")],
        [sg.Button("Save")],
    ],
    element_justification="right",
    expand_x=True,
    key="-Experience-",
    visible=False,
)
