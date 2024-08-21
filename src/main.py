from vyper import bot
from database import setup_db
from os import environ
import asyncio


def main():
    asyncio.run(setup_db())
    token = environ['DISCORD_TOKEN']
    bot.run(token)


if __name__ == "__main__":
    main()
