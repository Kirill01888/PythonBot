import discord
from discord.ext import commands
import random

def generate():
    str = random.choice(part1Text) + random.choice(part2Text) + random.choice(part3Text) + random.choice(part4Text)
    print (str)

client = discord.Client()

part1Text = ['Герои пришли в ',"Герои ушли от "]
part2Text = ["таверны ","шахты "]
part3Text = ["и перед ними открылся странный пейзаж ","и почуствовали облегчение "]
part4Text = ["но они хотели отдохнуть.","но они устали."]

helloWords = ['hi','hello']

@client.event
async def on_ready():
    print('Bot is working')
    generate()

@client.event
async def on_message(message):
    if message.author == client.user:
        return await message.channel.send('Hello')

    msg = message.content.lower()
    msg_list = msg.split

    if len(list(set(msg_list + helloWords))) < len(msg_list) + len(helloWords):
        await message.channel.send('Hello')

    if message.content.startswith('Hello'):
        await message.channel.send(f'Hello!{message.author.mention}')

    if message.content.startswith('Help'):
        await message.channel.send('Commands:')

    if message.content.startswith('Bye'):
        await message.channel.send('Bye')

client.run('')
