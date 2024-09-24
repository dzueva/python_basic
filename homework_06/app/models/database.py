import requests
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()



