import os

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from models import db, fetch_data, USERS_DATA_URL, POSTS_DATA_URL, User, Post
from views import views


def populate_db():
    users_data = fetch_data(USERS_DATA_URL)
    posts_data = fetch_data(POSTS_DATA_URL)

    with app.app_context():
        for user in users_data:
            new_user = User(
                id=user['id'],
                name=user['name'],
                username=user['username'],
                email=user['email']
            )
            db.session.add(new_user)

        for post in posts_data:
            new_post = Post(
                id=post['id'],
                user_id=post['userId'],
                title=post['title'],
                body=post['body']
            )
            db.session.add(new_post)

        db.session.commit()


load_dotenv(".env")

app = Flask(__name__,)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URI",
    "sqlite:///test.db",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.environ.get("FLASK_KEY")
app.register_blueprint(views)

db.app = app
db.init_app(app)

with app.app_context():
    db.create_all()
    populate_db()

migrate = Migrate(app, db, compare_type=True)


if __name__ == "__main__":
    app.run(debug=False)
