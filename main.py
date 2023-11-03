import discord
from discord.ext import commands
import os
print(os.listdir('image'))
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    with open('image/mem1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def mem_random(ctx):
    with open(f'image/{random.choice (os. listdir ("image"))}', "rb") as f:
              picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem_cat(ctx):
    with open(f'memcat/{random.choice (os. listdir ("memcat"))}', "rb") as f:
              picture = discord.File(f)
    await ctx.send(file=picture)
              
bot.run("ТОКЕН")
