#!/usr/bin/env python3

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
    
    fake_users = [User(name=fake.name()) for _ in range(5)]
    session.add_all(fake_users)
    session.commit()

    


