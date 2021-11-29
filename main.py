import discord
import random

# Генератор сценариев
def generate():
    part1Text = random.choice(part1Text_raw)
    part2Text = random.choice(part2Text_raw)
    part3Text = random.choice(part3Text_raw)
    part4Text = random.choice(part4Text_raw)

    # Исправление нелогичных связей
    # if part1Text == part1Text_raw[2]:
    #     part2Text = part2Text_raw[random.randint(2, 5)]
    # else:
    #     part2Text = part2Text_raw[random.randint(0, 1)]
    #
    # if part3Text == part3Text_raw[1]:
    #     part4Text = part4Text_raw[2]
    #
    # if part4Text == part4Text_raw[2]:
    #     part3Text = part3Text_raw[1]
    #
    # if part1Text == part1Text_raw[3]:
    #     part2Text = part2Text_raw[random.randint(6, 7)]
    #     part3Text = part3Text_raw[random.randint(0, 4)]
    #
    # if part3Text == part3Text_raw[2 or 4]:
    #     part4Text = part4Text_raw[random.randint(3, 4)]
    #
    # if part1Text == part1Text_raw[5]:
    #     part2Text = part2Text_raw[12]
    #     part3Text = part3Text_raw[5]
    #     part4Text = part4Text_raw[5]

    if part1Text == part1Text_raw[0]:
        part2Text = part2Text_raw[random.randint(0,1)]
        part3Text = part3Text_raw[random.randint(1,4)]
        if part3Text == part3Text_raw[3]:
            part4Text = part4Text_raw[3]
        elif part3Text == part3Text_raw[4]:
            part4Text = part4Text_raw[random.randint(3,4)]
        elif part3Text == part3Text_raw[1]:
            part4Text = part4Text_raw[2]
        else:
            part4Text = part4Text_raw[1]

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
part1Text_raw = ["Герои пришли в ", "Герои ушли от ", "Герои направились на ", "Герои спустились в ", "Герои поднялись на ", "Герои "]
part2Text_raw = ["шахты ", "пещеру ", "таверны ", "север ", "восток ", "юг ", "запад ", "расщелину ", "гору ", "холм ", "дерево ", "*ОГРОМНЫЙ* камень "]
part3Text_raw = ["и перед ними открылся странный пейзаж, ", "и почуствовали облегчение, ", "и ничего не обнаружили.", "и наткулись на ", "и увидели "]
part4Text_raw = ["он их удивил.", "однако они устали и хотели отдохнуть.", "хотя раслабляться было рано.", "монстров.", "страшные вещи..."]

helloWords = ["hi", "hello", 'privet', 'привет']
byeWords = ['bye', 'goodbye', 'пока', 'poka']
startWords = ['!начать', '!start', '!generate', '!сгенерировать']

# Определитель слов (Часть 2)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    listHello = split_strip(msg)
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
