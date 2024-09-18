import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_users_data(url: str = USERS_DATA_URL) -> list[dict]:
    data = await fetch_json(url)
    return data


async def fetch_post_data(url: str = POSTS_DATA_URL) -> list[dict]:
    data = await fetch_json(url)
    return data
