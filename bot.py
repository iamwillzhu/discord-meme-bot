import os
import discord

from datetime import datetime
from dotenv import load_dotenv
from collections import defaultdict
from models.expense_tracker import ExpenseTracker
from models.user import User
from controller import Controller
from view import View
from parser import Parser


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

set_one = defaultdict(int)
set_two = defaultdict(int)
set_one["Wei"] = 5
set_two["iamwill"] = -5

model = ExpenseTracker(
    users=[
        User(
            name="iamwill",
            expenses=set_one
        ),
        User(
            name="Wei",
            expenses=set_two
        )
    ]
)

view = View()
controller = Controller(model=model, view=view)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!Atlas"):
        parsed_message = Parser.parse_message(
            message=message.content)

        if parsed_message.command == "pay":
            response = controller.pay_user(
                caller=message.author,
                receiver=parsed_message.receiver,
                amount=parsed_message.amount
            )
        await message.channel.send(response)


client.run(TOKEN)
