import discord
from discord.ext import commands
  
client = discord.Client()

token = '...'

@client.event
async def on_ready():
    pfp_path = "tdkbot.png"
    with open(pfp_path, "rb") as pfp:
        await client.user.edit(password=None, avatar=pfp.read())
    print("profile picture changed")

client.run('n o')