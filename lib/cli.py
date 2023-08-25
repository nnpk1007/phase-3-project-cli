import re
from prettycli import red, yellow, blue
from simple_term_menu import TerminalMenu
from models import User, Item, Transaction


class Cli():

    def __init__(self):
        
        current_user = None

    
    def start(self):
        self.clear_screen()
        
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

        self.clear_screen()
        
        email = input("Please enter your email: ")
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                
        if re.fullmatch(regex, email):
            user = User.find_user_by_email(email)
            if user:
                self.current_user = user
                print(yellow(f"Hello, {user.name}!"))
                self.show_user_options()
            else:
                print(red("User not found. Please try again!"))
                self.start()
        else:
            print(red("Invalid email. Please try again"))
            self.start()

    
    def handle_sign_up(self):
        
        self.clear_screen()

        name = input("Enter your full name: ")
        email = input("Enter your email: ")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        user = User.find_user_by_email(email)

        if user:
            print(red("This email is already in used. Please sign up with another email"))
            self.start()
        else:
            if re.fullmatch(regex, email):
                user = User.create_user(name, email)

                self.current_user = user
                print(blue(f"Hello, {user.name}!"))

                self.show_user_options()
            else:
                print(red("Invalid email. Please try again!"))
                self.start() 


    def show_user_options(self):
        
        while True:
            
            options = ["Items On Sale","Search For Item", "Add Item For Sale", "Buy An Item", "Remove An Item", "Your Transactions", "Exit"]
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            
            if options[menu_entry_index] == "Items On Sale":
                self.items_on_sale()  
            elif options[menu_entry_index] == "Search For Item":
                self.search_for_item()  
            elif options[menu_entry_index] == "Add Item For Sale":
                self.add_item_for_sale()
            elif options[menu_entry_index] == "Buy An Item":
                self.buy_an_item()
            elif options[menu_entry_index] == "Remove An Item":
                self.remove_an_item()
            elif options[menu_entry_index] == "Your Transactions":
                self.your_transactions()
            else:
                self.exit()
                break


    def items_on_sale(self):

        self.clear_screen()            

        items = Item.show_items()

        if items:
            print(yellow("Items on sale:"))

            self.print_items(items)
        else:
            print("No items are available.")
    

    def search_for_item(self):
        self.clear_screen()
        
        search_item = input("What item are you looking for? ").lower()
        items = Item.show_items()

        matching_items = []
        for item in items:
            if search_item in item.title.lower().split():
                matching_items.append(item)
            
        #print(matching_items)

        if matching_items:
            print(yellow("Matching Items:"))
            self.print_items(matching_items)
            
        else:
            print(yellow("Item not found."))


    def print_items(self, items):

        for item in items:
                print(blue(f"Item: {item.title}"))
                print(f"ID: {item.id}")
                print(f"Description: {item.description}")
                print(f"Price: ${item.price}")
                user = User.find_user_by_seller_id(item.seller_id)
                print(f"Sold by: {user.name}")


    def add_item_for_sale(self):

        self.clear_screen()

        title = input("Item title: ")
        description = input("Description: ")
        # use while loop to check if price is a valid number
        while True:
            price = input("Price: $")
            if price.isdigit():
                break
            else:
                print(red("Invalid price. Please enter a valid number."))

        item = Item.add_item(title, description, price, seller_id=self.current_user.id)
        print(yellow("Item added."))
    

    def buy_an_item(self):

        self.clear_screen()
        self.items_on_sale()

        item_id = input(yellow("Enter the item id which you want to buy: "))
                
        item = Item.find_item_by_id(item_id)
        
        if not item:
            print(yellow("Item not found."))
        elif item.seller_id == self.current_user.id:
            print(red("You can not buy an item which is sold by yourself."))
        else:
            Transaction.add_transaction(item_id, self.current_user.id)
            Item.delete_item_by_id(item_id)
            print(blue("Item bought."))
    

    def remove_an_item(self):
        self.clear_screen()
        self.items_on_sale()

        item_id = input(yellow("Enter the item id which you want to remove: "))
                
        item = Item.find_item_by_id(item_id)

        if not item:
            print(yellow("Item not found."))
        elif item.seller_id != self.current_user.id:
            print(red("You can not remove an item which is sold by another user."))
        else:
            Item.delete_item_by_id(item_id)
            print(red("Item removed."))


    def your_transactions(self):

        self.clear_screen()

        transactions = Transaction.show_transactions(self.current_user.id)

        if len(transactions) == 0:
            print(yellow("You don't have any transaction.")        )
        else:
            print(blue("Your transactions:"))

            total_spent = 0

            for transaction in transactions:    
                print(yellow(f"Item: {transaction.item_title}"))
                print(f"Transaction amount: ${transaction.transaction_amount}")
                print(f"Transaction date: {transaction.transaction_date}")
                total_spent += transaction.transaction_amount
            
            print(blue(f"Total amount spent: ${total_spent}"))


    def exit(self):

        self.clear_screen()
        print(blue("Goodbye!"))

    
    def clear_screen(self):

        print("\n" * 40)

    
app = Cli()
app.start()
