import asyncio
import os
from typing import List

from jsonplaceholder_requests import fetch_users_data, fetch_post_data, USERS_DATA_URL, POSTS_DATA_URL
from models.base import Base
from models.user import User
from models.post import Post
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(url=PG_CONN_URI, echo=False)
Session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def fetch_users(session: AsyncSession, users_data: list[dict]) -> list[User]:
    users = [
        User(id=el["id"], username=el["username"], name=el["name"], email=el["email"])
        for el in users_data
    ]
    session.add_all(users)
    await session.commit()
    return users


async def fetch_posts(session: AsyncSession, posts_data: list[dict]) -> list[Post]:
    posts = [
        Post(user_id=el["userId"], id=el["id"], title=el["title"], body=el["body"])
        for el in posts_data
    ]
    session.add_all(posts)
    await session.commit()
    return posts


async def create_save_data():
    async with Session() as session:
        users_data: List[dict]
        posts_data: List[dict]

        users_data, posts_data = await asyncio.gather(
            fetch_users_data(USERS_DATA_URL),
            fetch_post_data(POSTS_DATA_URL)
        )

        await fetch_users(session=session, users_data=users_data)
        await fetch_posts(session=session, posts_data=posts_data)
