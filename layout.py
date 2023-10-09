import PySimpleGUI as sg
from utils import *

class Popup:
    def layout():
        layout = [[sg.Text('TXT Reader by: Vítor Moura and RafaelNST')],
                [sg.Button('Random choice'),
                sg.Button('Insert a name'),
                sg.Button('Remove a name'),
                sg.Button('View the content'),
                sg.Button('Exit')]]
        return layout
