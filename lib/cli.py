import re
from prettycli import red, yellow, blue
from simple_term_menu import TerminalMenu
from models import User, Item, Transaction


class Cli():

    def __init__(self):
        
        current_user = None

    
    def start(self):
        
        print(yellow("WELCOME TO FLATIRON MARKET PLACE"))
        options = ["Login", "Sign Up", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if options[menu_entry_index] == "Login":
            self.handle_login()
        elif options[menu_entry_index] == "Sign Up":
            self.handle_sign_up()
        else:
            self.exit()


    def handle_login(self):

        email = input("Please enter your email: ")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, email):
            user = User.find_user_by_email(email)
            self.current_user = user

            print(f"Hello, {user.name}!")
            self.show_user_options()
        else:
            print(red("User not found. Please try again!"))
            self.start()

    
    def handle_sign_up(self):

        name = input("Enter your full name: ")
        email = input("Enter your email: ")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.fullmatch(regex, email):
            user = User.create_user(name, email)

            self.current_user = user

            self.show_user_options()
        else:
            print("Invalid email. Please try again!")
            self.start() 

        print(f"Hello, {user.name}!")


    def show_user_options(self):
        
        options = ["Items On Sale", "Add Item For Sale", "Buy Item", "Show Transaction", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        
        if options[menu_entry_index] == "Items On Sale":
            items = Item.show_items()

            if items:
                print(yellow("Items on sale:"))

                for item in items:
                    print(blue(f"Item: {item.title}"))
                    print(f"Description: {item.description}")
                    print(f"Price: ${item.price}")
                    user = User.find_user_by_seller_id(item.seller_id)
                    print(f"Sold by: {user.name}")

                    
    def exit(self):
        print("Good bye!")
    
app = Cli()
app.start()
