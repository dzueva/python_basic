from models.base import Base
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    Text
)
from sqlalchemy.orm import relationship


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(200), nullable=False, default="Title")
    body = Column(Text, nullable=False, default="Body")

    user = relationship('User', back_populates='posts', uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(user_id={self.user_id}, id={self.id}, title={self.title!r}, body={self.body!r})"

    def __repr__(self):
        return str(self)
