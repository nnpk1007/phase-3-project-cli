from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    registration_date = Column(DateTime, default=func.now())

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
