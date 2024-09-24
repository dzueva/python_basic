from models.database import db
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, default="John Doe")
    username = db.Column(db.String(150), nullable=False, default="johndoe")
    email = db.Column(db.String(150), nullable=False, default="example@example.com")

    posts = relationship('Post', back_populates='user')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id!r}, name={self.name!r}, username={self.name!r}, email={self.email})"

    def __repr__(self):
        return str(self)
