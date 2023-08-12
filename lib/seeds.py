#!/usr/bin/env python3

import random
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import User, Item, Transaction, user_transaction

fake = Faker()


if __name__ == "__main__":
    engine = create_engine("sqlite:///data.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # clear old data
    session.query(User).delete()
    session.query(Item).delete()
    session.query(Transaction).delete()
    session.query(user_transaction).delete()

    print("Seeding data...")

    # create fake users
    fake_users = [User(name=fake.name()) for _ in range(5)]
    session.add_all(fake_users)
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
        # choose a random user 
        fake_user = random.choice(fake_users)

        item = Item(
            title=fake_item["title"], 
            description=fake_item["description"], 
            price=fake_item["price"], 
            seller_id=fake_user.id
            )
        
        session.add(item)
        session.commit()
            

    session.close()

    print("Done seeding")

    




