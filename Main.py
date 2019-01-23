import discord
from discord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
  print("Logged in as")
  print(bot.user.name)
  print(bot.user.id)
  
@bot.command()
async def leave(server: int):
  server = ctx.message.server(server)
  await bot.say("bye i'm leaving :)")
  await bot.leave(server)
  
@bot.command()
async def servers():
  servers = list(bot.servers)
  await bot.say("Connected on " + str(len(bot.servers)) + " servers:")
  await bot.say('\n'.join(server.id for server in servers))
  
bot.run(os.environ['BOT_TOKEN'])
