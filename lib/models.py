from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    registration_date = Column(DateTime, default=func.now())

    def __repr__(self):

        return f"<User {self.name} {self.registration_date}>"