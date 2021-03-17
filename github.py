import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'k!') 

@client.event
async def on_ready():
    print('its alive!!!!')

@client.command()
async def ping(ctx):
    await ctx.send(f'what the fuck do you want `{round(client.latency * 1000)} ms`')

client.run('bruh')