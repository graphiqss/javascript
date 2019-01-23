import discord
from discord.ext import commands

@bot.event
async def on_ready():

bot.run(os.environ['BOT_TOKEN'])
