import asyncio
import discord
import random
##from discord.ext import commands

# Генератор сценариев
def generate():
    part1Text = random.choice(part1Text_raw)
    part2Text = random.choice(part2Text_raw)
    part3Text = random.choice(part3Text_raw)
    part4Text = random.choice(part4Text_raw)

    # Исправление нелогичных связей
    if part1Text == part1Text_raw[2]:
        part2Text = part2Text_raw[random.randint(2, 5)]
    else:
        part2Text = part2Text_raw[random.randint(0, 1)]

    if part3Text == part3Text_raw[1]:
        part4Text = part4Text_raw[2]

    if part4Text == part4Text_raw[2]:
        part3Text = part3Text_raw[1]

    str = part1Text + part2Text + part3Text + part4Text

    return (str)

# Определитель слов (Часть 1)
def split_strip(message):
    m = message.split()
    list = []
    for msg in m:
        str = msg
        str = str.strip()
        list.append(str)
    return list

client = discord.Client()

# Лист ресурсов
part1Text_raw = ["Герои пришли в ", "Герои ушли от ", "Герои на правились на "]
part2Text_raw = ["таверны ", "шахты ", "север ", "восток ", "юг ", "запад "]
part3Text_raw = ["и перед ними открылся странный пейзаж, ", "и почуствовали облегчение, "]
part4Text_raw = ["однако они устали и хотели отдохнуть.", "он их удивил.", "хотя раслабляться было рано."]

helloWords = ["hi", "hello", 'privet', 'привет']
byeWords = ['bye', 'goodbye', 'пока', 'poka']
helpWords = ['!help', '!commands', '!помощь', '!команды']
startWords = ['!начать', '!start', '!generate', '!сгенерировать']

# Debug
@client.event
async def on_ready():
    print('Bot is working')
    print(generate())

# Определитель слов (Часть 2)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    listHello = split_strip(msg)
    listHelp = split_strip(msg)
    listBye = split_strip(msg)
    listStart = split_strip(msg)

    # Приветствие
    for h in listHello:
        if h in helloWords:
            if h == helloWords[3]:
                await message.channel.send(f'Привет, {message.author.mention}!')
            elif h == helloWords[2]:
                await message.channel.send(f'Privet, {message.author.mention}!')
            else:
                await message.channel.send(f'Hello, {message.author.mention}!')

    # Помощь
    for hp in listHelp:
        if hp in helpWords:
            if hp == helpWords[0 or 2]:
                await message.channel.send("Here's the list of commands: ")
                await message.channel.send(">!start, !generate - Generate the text")
                await asyncio.sleep(1)
                await message.channel.send("||That's all ¯\_(ツ)_/¯||")
            else:
                await message.channel.send("Вот список команд: ")
                await message.channel.send(">!начать, !сгенерировать - Сгенерировать")
                await asyncio.sleep(1)
                await message.channel.send("||Это всё ¯\_(ツ)_/¯||")

    # Прощание
    for b in listBye:
        if b in byeWords:
            if b == byeWords[2]:
                await message.channel.send(f'Пока, {message.author.mention}! Удачи!')
            elif b == byeWords[3]:
                await message.channel.send(f'Poka, {message.author.mention}! Udachi!')
            else:
                await message.channel.send(f'Bye, {message.author.mention}! Good luck for you!')

    # Запуск
    for s in listStart:
        if s in startWords:
            await message.channel.send(generate())

client.run('')
