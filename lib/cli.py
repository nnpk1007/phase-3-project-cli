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
        
        while True:
            options = ["Items On Sale", "Add Item For Sale", "Buy An Item", "Your Transactions", "Exit"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            
            if options[menu_entry_index] == "Items On Sale":
                items = Item.show_items()

                if items:
                    print(yellow("Items on sale:"))

                    for item in items:
                        print(blue(f"Item: {item.title}"))
                        print(f"ID: {item.id}")
                        print(f"Description: {item.description}")
                        print(f"Price: ${item.price}")
                        user = User.find_user_by_seller_id(item.seller_id)
                        print(f"Sold by: {user.name}")
                else:
                    print("No items are available")

            elif options[menu_entry_index] == "Add Item For Sale":
                title = input("Item title: ")
                description = input("Description: ")
                price = input("Price: $")

                item = Item.add_item(title, description, price, seller_id=self.current_user.id)
                print(yellow("Item added"))
            
            elif options[menu_entry_index] == "Buy An Item":
                item_id = input("Enter the item id which you want to buy: ")

                Transaction.add_transaction(item_id, self.current_user.id)
                Item.delete_item_by_id(item_id)

            elif options[menu_entry_index] == "Your Transactions":
                transactions = Transaction.show_transactions(self.current_user.id)
                print(blue("Your transactions:"))
                for transaction in transactions:
                    print(yellow(f"Item: {transaction.item_title}"))
                    print(f"Transaction amount: {transaction.transaction_amount}")
                    print(f"Transaction date: {transaction.transaction_date}")

            else:
                self.exit()
                break

    
    def exit(self):

        print(f"Good bye {self.current_user.name}!")
    
app = Cli()
app.start()
