from models.database import db
from sqlalchemy.orm import relationship


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(200), nullable=False, default="Title")
    body = db.Column(db.Text, nullable=False, default="Body")

    user = relationship('User', back_populates='posts')

    def __str__(self):
        return f"{self.__class__.__name__}(user_id={self.user_id}, id={self.id}, title={self.title!r}, body={self.body!r})"

    def __repr__(self):
        return str(self)
