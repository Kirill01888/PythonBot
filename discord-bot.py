import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.CRITICAL)
logging.basicConfig(level=logging.ERROR)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send((f'{message.author.mention}Hello!'))

    if message.content.startswith('.'):
        await message.channel.send('')

    if message.content.startswith('.'):
        await message.channel.send('')

    if message.content.startswith('.'):
        await message.channel.send('')

    if message.content.startswith('.'):
        await message.channel.send('')

client.run('OTExMjI4MTAwODU4MjM2OTQ5.YZeVTQ.mmdgBqCdiDzFJRZdyK__T9Ud78Q')