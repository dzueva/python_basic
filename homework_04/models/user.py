from models.base import Base
from sqlalchemy import (
    Column,
    String
)
from sqlalchemy.orm import relationship


class User(Base):
    name = Column(String(30), nullable=False, default="John Doe")
    username = Column(String(150), nullable=False, default="johndoe")
    email = Column(String(150), nullable=False, default="example@example.com")

    posts = relationship('Post', back_populates='user', uselist=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, username={self.name!r}, email={self.email})"

    def __repr__(self):
        return str(self)
