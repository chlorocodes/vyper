import discord
import asyncio
import aiosqlite

db_file = "vyper.db"


async def setup_db():
    async with aiosqlite.connect(db_file) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY, username TEXT, display_name TEXT)
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS saved_messages 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, message TEXT, user_id INTEGER)
        """)

        await db.commit()

        print("Database tables have been created!")


async def save_user_to_db(user_id, username, display_name):
    async with aiosqlite.connect(db_file) as db:
        await db.execute("""
            INSERT OR IGNORE INTO users (id, username, display_name)
            VALUES (?, ?, ?)
        """, (user_id, username, display_name))

        await db.commit()


async def save_message_to_db(message, user_id):
    async with aiosqlite.connect(db_file) as db:
        await db.execute("""
            INSERT INTO saved_messages (message, user_id)
            VALUES (?, ?)
        """, (message, user_id))

        await db.commit()


async def load_all_messages_for_user(user):
    async with aiosqlite.connect(db_file) as db:
        async with db.execute('SELECT * FROM saved_messages WHERE user_id = ?',  (user.id,)) as cursor:
            messages = []
            async for row in cursor:
                msg = row[1]
                messages.append(msg)
            return messages
