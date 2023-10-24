import PySimpleGUI as sg

# Themeing
sg.theme('Black')
sg.theme_background_color('#000000')
sg.theme_text_color('#00FF00')
sg.theme_input_background_color('#000000')
sg.theme_input_text_color('#00FF00')
sg.theme_button_color('#00FF00')

# Functions
def Go_To(x):
    x()



# Chapters
def Prologue():
    print('Hello!')
    # Prologue
    Indhold = [ [sg.Text("For nogle dage siden modtog du et brev fra din fætter, Karsten, hvori han inviterede dig herhen for at fejre din fødselsdag. Uden tvivl havde hand på sinde at få dig med ud at jage spor på Ebonholms lokale søuhyr: 'Vækkeren'.", font=('Oswald', 11, 'bold'), size=(80,3),)],
                [sg.Input(size=(80,1), key='-Input-')],
                [sg.Text(size=(40,1), key='-Output-')],
                [sg.Button('Ok'), sg.Button('Afslut'),] 
            ]

    window = sg.Window('Ebonholm Prologue', Indhold, text_justification='center', element_justification='center')



# Start Menu
Indhold = [ [sg.Text("Ebonholm", font=('Oswald', 18, 'bold'), size=(80,2),)],
            [sg.Button('New Game', font=('Oswald', 10, 'bold')), sg.Button('Load Game',font=('Oswald', 10, 'bold')),] 
        ]

window = sg.Window('Ebonholm Start Menu', Indhold, text_justification='center', element_justification='center')

while True:
    event, values = window.read()
    break
if event == 'New Game':
    # Overwrite Saved Chapter
    f = open('SaveData_Chapter.txt', 'w')
    f.write("Prologue")
    f.close()
    
    # Overwrite Saved States
    f = open('SaveData_States.txt', 'w')
    f.write("")
    f.close()
    window.close
    Go_To(Prologue)
        