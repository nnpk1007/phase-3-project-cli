#!/usr/bin/env python3

import random
from faker import Faker
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from session import session

from models import User, Item, Transaction

fake = Faker()


if __name__ == "__main__":
    # engine = create_engine("sqlite:///data.db")
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # clear old data
    session.query(User).delete()
    session.query(Item).delete()
    session.query(Transaction).delete()

    print("Seeding data...")

    # create fake users
    fake_users = []
    for _ in range(5):
        name = fake.name()
        email = name.lower().replace(" ", "_") + "@gmail.com"
        
        fake_user = User(name=name, email=email)
        fake_users.append(fake_user)

        session.add(fake_user)
        session.commit()
    
    # create fake items
    fake_items = [
        {"title":"iPhone 13", "description":"Like new", "price":700},
        {"title":"Book", "description":"Used", "price":10},
        {"title":"Sony TV", "description":"Used", "price":500},
        {"title":"Table", "description":"Used", "price":40},
        {"title":"Apple Watch", "description":"Used", "price":300},
    ]

    # https://realpython.com/python-zip-function/
    for fake_user, fake_item  in zip(fake_users, fake_items):
        # choose a random seller 
        random_seller = random.choice(fake_users)

        item = Item(
            title=fake_item["title"], 
            description=fake_item["description"], 
            price=fake_item["price"], 
            seller_id=random_seller.id
            )
        
        session.add(item)
        session.commit()

        # fake transaction is used at the beginning when I first created the tables to test relationships
        # exclude the seller from the buyer
        # buyers = [user for user in fake_users if user != random_seller]   
        # # choose a random buyer
        # random_buyer = random.choice(buyers)

        # fake_transaction = Transaction(
        #     transaction_amount=fake_item["price"],
        #     item_id=item.id,
        #     buyer_id=random_buyer.id
        # )

        # session.add(fake_transaction)
        # session.commit()

    session.close()

    print("Done seeding.")

   #import ipdb; ipdb.set_trace()

    




