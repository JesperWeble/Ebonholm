import PySimpleGUI as sg
import os.path

# Themeing
sg.theme('Black')
sg.theme_background_color('#000000')
sg.theme_text_color('#00FF00')
sg.theme_input_background_color('#000000')
sg.theme_input_text_color('#00FF00')
sg.theme_button_color('#00FF00')

event = 0
# Functions
def Go_To(x):
    x()

def Help():
    sg.popup('Du kan bruge følgende commandoer: look around, use, take, give, go to, talk to')


# Chapters
def Prologue():
    # Prologue
    Indhold = [ [sg.Text("For nogle dage siden modtog du et brev fra din fætter, Karsten, hvori han inviterede dig hjem til sig selv i den gudsforladte landsby ved navn Ebonholm. for at fejre din fødselsdag. Uden tvivl havde hand på sinde at få dig med ud at jage spor på Ebonholms lokale søuhyr: 'Vækkeren'.", font=('Oswald', 11, 'bold'), size=(80,3),)],
                [sg.Text("Karsten var en mærkelig fyr. Han boede ude på bøhlandet efter at han havde valgt at isolere sig fra den bræde omverden. Han var blevet overbevist om at duer var overvågningsrobotter bygget af regeringen for at holde øje med ham og at verden var styret af øglemænd. Han havde forståeligt nok ingen venner, men havde vist fundet sig godt derude blandt de andre landsbytosser.", font=('Oswald', 11, 'bold'), size=(80,5),)],
                [sg.Text("Ærligt talt var du ikke meget for at mødes med ham, men Karsten var din eneste levende familie. Da du var lille forsvandt din mor sporløst, hun var taget ud på havet i søgen efter et eller andet, folk mente hun var blevet skør efter hendes mand forlod hende. Hendes mand, din far, ham havde du aldrig rigtig kendt, han forlod familien sammen med en anden kvinde da du var helt lille.", font=('Oswald', 11, 'bold'), size=(80,7),)],
                [sg.Text("Men nu var du har altså, hvorvidt om du kunne lide det eller ej, havde du sat nøglen i bilen, og kørt hele den lange vej ud til dette forfaldne sted. Du træder ud af din bil og får kuldegysninger i det at den ækle lugt af fisk og gødning rammer dine næsebor. Landsbyen ligger på en lille ø i midten af en stor sø.", font=('Oswald', 11, 'bold'), size=(80,3),)],
                [sg.Text("Du står på en lille parkeringsplads ved en tankstation, der er én anden bil udover din egen parkeret her. Asfalten ender her, men en smal sti fører videre ned mod færgen der kan sejle dig ud til landsbyen.", font=('Oswald', 11, 'bold'), size=(80,3),)],
                [sg.Input(size=(80,1), key='-Input-')],
                [sg.Text(size=(40,1), key='-Output-')],
                [sg.Button('Ok'), sg.Button('Afslut'), sg.Button('Help')] 
            ]

    window = sg.Window('Ebonholm Prologue', Indhold, text_justification='center', element_justification='center')
    event, values = window.read()




def Start():
    # Start Menu
    Indhold = [ [sg.Text("Ebonholm", font=('Oswald', 18, 'bold'), size=(80,2),)],
                [sg.Button('New Game', font=('Oswald', 10, 'bold')), sg.Button('Load Game',font=('Oswald', 10, 'bold')),] 
            ]

    window = sg.Window('Ebonholm Start Menu', Indhold, text_justification='center', element_justification='center')
    event, values = window.read()

    if event == 'Load Game' and os.path.isfile('SaveData_Chapter.txt')==True:
        window.close()
        f = open('SaveData_Chapter.txt', 'r')
        Destination = f.readline()
        f.close
        Go_To(globals()[Destination])
        
    else:
        window.close()
        # Overwrite Saved Chapter
        f = open('SaveData_Chapter.txt', 'w')
        f.write("Prologue")
        f.close()

        # Overwrite Saved States
        f = open('SaveData_States.txt', 'w')
        f.write("")
        f.close()
        Go_To(Prologue)        



Start()

if event == 'Help':
    Help()