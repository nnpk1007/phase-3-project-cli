import re
from prettycli import red
from simple_term_menu import TerminalMenu
from models import User, Item, Transaction


class Cli():

    def __init__(self):
        
        user = None

    
    def start(self):
        
        print("WELCOME TO FLATIRON MARKET PLACE")
        options = ["Login", "Sign Up", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()


    
app = Cli()
app.start()
