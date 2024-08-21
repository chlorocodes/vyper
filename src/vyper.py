import os
import discord
import aiosqlite
import database

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = discord.Bot(intents=intents, description='Vyper bot')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!'):
        await on_command(message)


async def on_command(message):
    text = message.content
    command = text.split(' ')[0]

    if command == '!save':
        await save_message_for_user(message)
    elif command == '!load':
        await load_all_saved_messages_for_user(message)


async def save_message_for_user(message):
    command, *words = message.content.split(' ')
    text_to_save = ' '.join(words)
    user = message.author
    await database.save_user_to_db(user.id, user.name, user.display_name)
    await database.save_message_to_db(text_to_save, user.id)
    await message.reply('I have saved your message to the database!')


async def load_all_saved_messages_for_user(message):
    user = message.author
    user_saved_messages = await database.load_all_saved_messages_for_user(message.author)
    embed = discord.Embed(
        title="Saved Messages From " + user.display_name,
        description="Here are all the saved messages for " + user.display_name,
        color=discord.Colour.green(),
    )

    for msg in user_saved_messages:
        embed.add_field(
            name=user.display_name,
            value=msg,
            inline=False
        )

    await message.reply(embed=embed)
