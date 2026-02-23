import discord
from discord.ext import commands
from bot_logic import gen_pass, gen_emodji, flip_coin
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def gen_password(ctx, length: int):
    password = gen_pass(length)
    return await ctx.send(f'Password generata: {password}')

@bot.command()
async def emoji(ctx):
    emoji = gen_emodji()
    return await ctx.send(f'Ecco un emoji random: {emoji}')

@bot.command()
async def flip(ctx):
    await ctx.send("Sto lanciando la moneta!")
    for _ in range(3):
        await ctx.send(".")
        time.sleep(0.3) 

    risultato = flip_coin()
    await ctx.send(f"La moneta cade su: {risultato}")
bot.run("")
