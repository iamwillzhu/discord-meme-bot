import os
import discord

from dotenv import load_dotenv
from meme import Meme


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'!{client.user.name}'):
        random_meme = Meme.create_random_meme(message.author.display_name)
        response = random_meme.generate_file()
        await message.channel.send(file=discord.File(response))


client.run(TOKEN)
