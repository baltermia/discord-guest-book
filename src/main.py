import discord
import os
from dotenv import load_dotenv
from db import get_conn
import mysql.connector

# env api
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# discord api
client = discord.Client()

# mysql api
conn = get_conn()
cursor = conn.cursor()

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
    try:
        sql = "INSERT INTO guests (ServerID, Benutzername, Nachricht, Timestamp) VALUES (%s, %s, %s, %s)"
        val = (msgObj.guild.id, msgObj.author.id, text, msgObj.created_at)
        
        cursor.execute(sql, val)
        
        conn.commit()
        
        await msgObj.channel.send(f"GuestBook Entry successfully created.")
    except Error as error:
        await msgObj.channel.send(f"An unexpected Error occured. GuestBook Entry couldn't be created.")

client.run(token)