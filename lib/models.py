from sqlalchemy import Table, Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    registration_date = Column(DateTime, default=func.now())

    # define relationship with Item
    # an item is listed by a user and a user can list many item for sell (user is on "one" side, and item is on "many" side)
    items = relationship("Item", backref=backref("user"))
    # define relationship with transaction
    # a transaction is purchased by a user and a user can have many transactions (user is on "one" side, and transaction is on "many" side)
    transactions = relationship("Transaction", backref=backref("user"))

    def __repr__(self):

        return f"<User {self.id} {self.name} {self.registration_date}>"


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


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer(), primary_key=True)
    transaction_amount = Column(Integer())
    transaction_date = Column(DateTime, default=func.now())

    item_id = Column(Integer(), ForeignKey("items.id"))
    buyer_id = Column(Integer(), ForeignKey("users.id"))

    def __repr__(self):

        return f"<Transaction {self.id} {self.transaction_amount} {self.transaction_date} {self.item_id} {self.buyer_id}>"

