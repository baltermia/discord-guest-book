import discord
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    msg = message.content
    author = message.author

    if not msg.startswith("-"):
        return

    if author == client.user:
        return

    await command(msg, message)

async def command(msg, msgObj):
    # Remove first letter
    strs = msg.split(" ", 1)
    
    cmd = strs[0]
    text = strs[1]

    cmd = {
        "new": await new(text, msgObj)
    }

async def new(text, msgObj):
    await msgObj.channel.send(f"Message: {text}")

client.run(token)