import re
from prettycli import red
from simple_term_menu import TerminalMenu
from models import User, Item, Transaction


class Cli():

    def __init__(self):
        
        current_user = None

    
    def start(self):
        
        print("WELCOME TO FLATIRON MARKET PLACE")
        options = ["Login", "Sign Up", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Login":
            self.handle_login()


    def handle_login(self):
        email = input("Please enter your email: ")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, email):
            user = User.find_user_by_email(email)
            self.current_user = user

            print(f"Hello, {user.name}")
        else:
            print("User not found. Please try again!")
            self.start()
    
app = Cli()
app.start()
