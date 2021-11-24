import discord
from discord.ext import commands
import random

def generate():
    str = random.choice(part1Text) + random.choice(part2Text) + random.choice(part3Text) + random.choice(part4Text)
    print (str)

def split_strip(message):
    m = message.split()
    list = []
    for msg in m:
        str = msg
        str = str.strip()
        list.append(str)
    return list

client = discord.Client()

part1Text = ['Герои пришли в ', "Герои ушли от "]
part2Text = ["таверны ", "шахты "]
part3Text = ["и перед ними открылся странный пейзаж ", "и почуствовали облегчение "]
part4Text = ["но они хотели отдохнуть.", "но они устали."]

helloWords = ["hi", "hello",'privet','привет']
byeWords = ['bye','goodbye','пока','poka']
helpWords = ['help','commands','помощь','команды']

@client.event
async def on_ready():
    print('Bot is working')
    generate()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content.lower()

    listHello = split_strip(msg)
    listHelp = split_strip(msg)
    listBye = split_strip(msg)

    for i in listHello:
        if i in helloWords:
            await message.channel.send(f'Hello!{message.author.mention}')

    for o in listHelp:
        if o in helpWords:
            await message.channel.send('Commands: ')

    for p in listBye:
        if p in byeWords:
            await message.channel.send(f'Bye {message.author.mention} good luck for you')


client.run('')
