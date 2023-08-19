from sqlalchemy import Table, Column, Integer, String, DateTime, func, ForeignKey, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///data.db")
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(), unique=True)
    registration_date = Column(DateTime, default=func.now())

    # define relationship with Item
    # an item is listed by a user and a user can list many item for sell (user is on "one" side, and item is on "many" side)
    items = relationship("Item", backref=backref("user"))
    # define relationship with transaction
    # a transaction is purchased by a user and a user can have many transactions (user is on "one" side, and transaction is on "many" side)
    transactions = relationship("Transaction", backref=backref("user"))


    def __repr__(self):

        return f"<User {self.id} {self.name} {self.email} {self.registration_date}>"


    @classmethod
    def find_user_by_email(cls, email):

        user = session.query(cls).filter(cls.email == email).first()

        return user


    @classmethod
    def find_user_by_seller_id(cls, seller_id):

        user = session.query(cls).filter(cls.id == seller_id).first()

        return user
        

    @classmethod
    def create_user(cls, name, email):

        user = cls(name=name, email=email)

        session.add(user)
        session.commit()

        return user


class Item(Base):

    __tablename__ = "items"

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    description = Column(String())
    price = Column(Integer())
    listing_date = Column(DateTime, default=func.now())

    seller_id = Column(Integer(), ForeignKey("users.id"))


    def __repr__(self):

        return f"<Item {self.id} {self.title} {self.description} {self.price} {self.listing_date} {self.seller_id}>"


    @classmethod
    def show_items(cls):

        items = session.query(cls).all()
        
        return items


    @classmethod
    def add_item(cls, title, description, price, seller_id):

        item = cls(title=title, description=description, price=price, seller_id=seller_id)
        session.add(item)
        session.commit()

        return item


    @classmethod
    def find_item_by_id(cls, item_id):

        item = session.query(Item).filter(Item.id == item_id).first()

        return item

    @classmethod
    def delete_item_by_id(cls, item_id):

        item = session.query(cls).filter(cls.id == item_id).first()

        if item:
            session.delete(item)
            session.commit()

            print("Item bought")
        else:
            print("Item not found")
            

class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer(), primary_key=True)
    transaction_amount = Column(Integer())
    transaction_date = Column(DateTime, default=func.now())
    item_title = Column(String())

    item_id = Column(Integer(), ForeignKey("items.id"))
    buyer_id = Column(Integer(), ForeignKey("users.id"))
    
    
    def __repr__(self):

        return f"<Transaction {self.id} {self.transaction_amount} {self.transaction_date} {self.item_id} {self.buyer_id}>"

    @classmethod
    def add_transaction(cls, item_id, buyer_id):

        item = Item.find_item_by_id(item_id)

        transaction = cls(transaction_amount=item.price, item_title=item.title, item_id=item_id, buyer_id=buyer_id )

        session.add(transaction)
        session.commit()

        return transaction


    @classmethod
    def show_transactions(cls, buyer_id):
        
        transactions = session.query(Transaction).filter(cls.buyer_id == buyer_id).all()

        return transactions