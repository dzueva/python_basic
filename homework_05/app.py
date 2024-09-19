from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", endpoint="index")
def index():
    return render_template("index.html")


@app.route("/about/", endpoint="about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5050)
