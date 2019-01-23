import discord
from discord.ext import commands

@bot.event
async def on_ready():
  print("Logged in as")
  print(bot.user.name)
  print(bot.user.id)
  
@bot.command(pass_context=True)
async def leave(ctx, server: id):
  server = ctx.message.server.id
  await bot.get_server(server)
  await bot.leave(server)
  
bot.run(os.environ['BOT_TOKEN'])
