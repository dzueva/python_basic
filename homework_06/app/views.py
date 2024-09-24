from flask import Blueprint, render_template, flash, redirect, request, url_for
from models import Post, User, db
from sqlalchemy.exc import DatabaseError

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"], endpoint="index")
def index():
    posts = Post.query.all()
    users = User.query.all()
    return render_template(
        "index.html",
        posts=posts,
        users=users,
    )


@views.route("/create_post", methods=["POST"])
def create_post():
    title = request.form.get("title")
    body = request.form.get("body")
    user_id = request.form.get("user_id")

    if not (title and body and user_id):
        return "Missing data for post creation!", 400

    new_post = Post(
        title=title,
        body=body,
        user_id=user_id,
    )
    db.session.add(new_post)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error: {str(e)}", 500

    return redirect("/")


@views.errorhandler(DatabaseError)
def handle_database_error(error):
    flash("oops! no db connection!", "danger")
    return redirect("/")
