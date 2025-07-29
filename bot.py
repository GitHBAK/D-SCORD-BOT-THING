import discord
from discord.ext import commands
import requests
import random
import string
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yaptık.")

@bot.event
async def on_member_join(member):
    kanal = discord.utils.get(member.guild.text_channels, name='general')
    if kanal:
        await kanal.send(f"👋 Hoş geldin, {member.mention}! Sunucumuza katıldığın için mutluyuz!")

@bot.command()
async def ordek(ctx):
    try:
        res = requests.get("https://random-d.uk/api/random")
        data = res.json()
        await ctx.send(data['url'])
    except Exception as e:
        await ctx.send(f"Hata oluştu: {e}")

@bot.command()
async def mem(ctx):
    try:
        klasor = 'images'
        if not os.path.exists(klasor):
            await ctx.send("❌ `images` klasörü bulunamadı.")
            return

        rarity_pool = []

        mem_rarity = {
            "mem1.png": "common",
            "mem2.png": "common",
            "mem3.png": "rare",
            "mem4.png": "legendary"
        }

        rarity_weights = {
            "common": 8,
            "rare": 2,      
            "legendary": 0.5
        }

        for filename, rarity in mem_rarity.items():
            if os.path.exists(os.path.join(klasor, filename)):
                weight = rarity_weights.get(rarity, 1)
                rarity_pool.extend([filename] * int(weight * 10))  # Ağırlığı büyüt

        if not rarity_pool:
            await ctx.send("Klasörde geçerli mem bulunamadı.")
            return

        secilen = random.choice(rarity_pool)
        with open(os.path.join(klasor, secilen), 'rb') as f:
            await ctx.send(file=discord.File(f, filename=secilen))

    except Exception as e:
        await ctx.send(f"Hata oluştu: {e}")


@bot.command()
async def sifre(ctx, uzunluk: int = 12):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    await ctx.send(f"Rastgele Şifre: `{sifre}`")

@bot.command()
async def emoji(ctx):
    emojiler = ['😀', '😎', '😂', '😈', '👻', '🤖', '🐍', '🍀', '🔥', '⭐']
    await ctx.send(random.choice(emojiler))

@bot.command()
async def yardim(ctx):
    mesaj = (
        "**Mevcut Komutlar:**\n"
        "`!ordek` – Rastgele ördek resmi gönderir 🦆\n"
        "`!meme` – Rastgele meme paylaşır 😂\n"
        "`!sifre [uzunluk]` – Rastgele şifre oluşturur 🔐 (Varsayılan: 12)\n"
        "`!emoji` – Rastgele emoji gönderir 😎\n"
        "`!yazitura` – Yazı mı tura mı atar 🎲\n"
        "`!bye` – Bot gülümseyen emoji gönderir 🙂\n"
        "`!yardim` – Bu mesajı gösterir 📝"
    )
    await ctx.send(mesaj)

@bot.command()
async def yazitura(ctx):
    sonuc = random.choice(['Yazı', 'Tura'])
    await ctx.send(sonuc)

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

bot.run("bot_token")
