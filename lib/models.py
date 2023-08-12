from sqlalchemy import Table, Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()


# a user can have many transactions and a transaction can be involed in many user(seller and buyer)
user_transaction = Table(
    "user_transactions",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("transaction_id", ForeignKey("transactions.id"), primary_key=True),
    extend_existing=False,
)


class User(Base):

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    registration_date = Column(DateTime, default=func.now())

    # define relationship with Item
    # am item is listed by a user and a user can list many item for sell ( user is on "one" side, and item is on "many" side)
    items = relationship("Item", backref="user")
    transactions = relationship("Transaction", secondary=user_transaction, back_populates="users")

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

    #user = relationship("User", back_populates="items")

    def __repr__(self):

        return f"<Item {self.id} {self.title} {self.description} {self.price} {self.listing_date} {self.seller_id}>"


class Transaction(Base):

    __tablename__ = "transactions"

    id = Column(Integer(), primary_key=True)
    transaction_amount = Column(Integer())
    transaction_date = Column(DateTime, default=func.now())

    item_id = Column(Integer(), ForeignKey("items.id"))
    buyer_id = Column(Integer(), ForeignKey("users.id"))

    users = relationship("User", secondary=user_transaction, back_populates="transactions")

    def __repr__(self):

        return f"<Transaction {self.id} {self.transaction_amount} {self.transaction_date} {self.item_id} {self.buyer_id}>"

