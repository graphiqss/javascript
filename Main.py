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
  
@bot.command(pass_context=True)
async def leave(ctx, server: int):
  server = bot.get_server(int)
  await bot.send_message(server, "bye Im leaving")
  await bot.leave_server(server)
  
@bot.command()
async def servers():
  servers = list(bot.servers)
  await bot.say("Connected on " + str(len(bot.servers)) + " servers:")
  await bot.say('\n'.join(server.id for server in servers))
  
bot.run(os.environ['BOT_TOKEN'])
