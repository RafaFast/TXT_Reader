import PySimpleGUI as sg
from random import choice

class Tools:
    def open_file_read(arch_name):
        with open(arch_name) as archive:
            return archive.read()
        
    def open_file_readlines(arch_name):
        with open(arch_name) as archive:
            return archive.readlines()
    
    def archive_name() -> str:
        "Ask the archive file name to the user"
        while True:
            ARCH_NAME = sg.popup_get_text('Enter the archive name (without the file type)').strip() + ".txt"

            if ARCH_NAME == ".txt":
                sg.popup("Invalid archive name")
            else:
                return ARCH_NAME

class Functs:
    EMPTY = ""
    def add(arch_name, name):
        "Add a word to a txt file"

        with open(arch_name, 'a') as archive:
            rows = Tools.open_file_read(arch_name)

            # Write a formated name on the txt file depending of its state
            if name != Functs.EMPTY:
                if rows == Functs.EMPTY:
                    archive.write(name)
                else:
                    archive.write(f'\n{name}')
            else:
                sg.popup("Valid name required")


    def pick_random(arch_name) -> str:
        "Pick a random word from a txt file"

        rows = Tools.open_file_readlines(arch_name)
        return choice(rows).strip()

    def remove(arch_name, chosen) -> None:
        "Remove a name from a txt file"

        # Rows and input treatment
        if chosen.strip() != Functs.EMPTY:
            rows = Tools.open_file_readlines(arch_name)

            # Add every word from 'arch_name', not being the chosen one, to 'rows'
            rows = [name.strip() for name in rows if name.strip() != chosen]

            # Iterate 'rows' and write it formated on the txt file depending of its state
            with open(arch_name, 'w') as archive:
                for name in rows:
                    if rows.index(name) == len(rows)-1:
                        archive.write(name)
                    else:
                        archive.write(name + '\n')
        else:
            sg.popup("Enter a valid name")

