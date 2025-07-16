import discord
import random
from bot_mantik import gen_pass

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!sifre'):
        await message.channel.send(gen_pass(10))
    
    elif message.content.startswith('!bye'):
        await message.channel.send("\U0001f642")
    
    elif message.content.startswith('!yazitura'):
        sonuc = random.choice(['Yazı', 'Tura'])
        await message.channel.send(sonuc)

    elif message.content.startswith('!emoji'):
        emojiler = ['😀', '😎', '😂', '😈', '👻', '🤖', '🐍', '🍀', '🔥', '⭐']
        await message.channel.send(random.choice(emojiler))
    
    else:
        await message.channel.send(message.content)

client.run("TOKENIN_BURAYA")
