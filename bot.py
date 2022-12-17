import json
import os,asyncio,sys

import discord
from discord.ext import commands

with open("config.json", "r", encoding="UTF-8") as file:
    config = json.load(file)

bot = commands.Bot(help_command=None, intents=discord.Intents.all())

@bot.event
async def on_ready():
    try:
        guild = await bot.fetch_guild(config["guild"])
    except:
        print("錯誤:找不到群組")
        await asyncio.sleep(10)
        await sys.exit()
    else:
        game = discord.Game(F"{guild.name} 專用金錢機器人")
        await bot.change_presence(status=discord.Status.online, activity=game)
        print(f">>{bot.user}上線<<")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'✅   已加載 {filename}')
        except Exception as error:
            print(f'❎   {filename} 發生錯誤  {error}')

bot.run(config["token"])