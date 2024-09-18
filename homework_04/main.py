import asyncio

from models import create_tables, create_save_data


async def async_main():
    await create_tables()
    await create_save_data()


async def main():
    await async_main()


if __name__ == "__main__":
    asyncio.run(main())
