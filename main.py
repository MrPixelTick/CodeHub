# CodeHUB Info
#
# Made By :
# MrPixelTick#0001[Owner], Hydra#4179[Co-Owner]
#
#CodeHUB Version :
#1.3.1
#
#Language :
#Python -> Discord.PY

#Variables

import os
import discord
from webserver import keep_alive
from discord.ext import commands, tasks
token = os.environ['token']
import logging
import requests
from bs4 import BeautifulSoup
from itertools import cycle


#Prefix & Status

client = commands.Bot(command_prefix = "!", status=discord.Status.idle)
status = cycle(['Made by MrPixelTick#0001, Hydra#4179 🎓', 'Im here to help you learn code! ⭐', 'Use !help for commands! 📜', 'The bot is in beta. ⏳', 'We hope you enjoy your experience with our bot 💖'])
client.remove_command('help')

#OnReady

@client.event #decorator for something happens
async def on_ready(): #asyncronious function, multithread
	change_status.start()
	#DiscordComponents(client)
	print("Code Hub Console\n\nLogged In As | Code Hub#4276\nUser ID | 871677834551246888\n\nLogging Started\n\n")

#Docs

def get_w3school_docs(parameter):
  try: #note: python_().asp
      url = ("https://www.w3schools.com/python/python_" + str(parameter)) + ".asp"
      res = requests.get(url)
      if res.status_code == 404:
        raise Exception
      return url
  except Exception:
      return ":warning: The docs could not be found or CodeHub messed up."

@client.command()
async def docs(ctx,arg1):
  embedVar = discord.Embed(title="CodeHub | Docs",description=arg1.capitalize() + ":\n"  + " " + get_w3school_docs(arg1),color=0x61FBFB)
  embedVar.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
  await ctx.send(embed=embedVar)

#Format

@client.command()#aliases=['formatpy', 'formatpython']
async def format(ctx,*,arg1): 
  try:
    splitted = arg1.split(" ")
    
    await ctx.send("```" + splitted[0] +"\n" + arg1[len(splitted[0]):] + "```")
  #await ctx.send("```"+arg1 +"\n" + arg2 + "```")
  except Exception:
    print(":warning: The function could not be found or CodeHub messed up")

#Logs

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('Time : %(asctime)s | Type : %(levelname)s | Name : %(name)s | Message : %(message)s'))
logger.addHandler(handler)

#Ping

@client.command()
async def ping(ctx):
	embed = discord.Embed(title="CodeHub | Ping",description=f"{round(client.latency * 1000)}ms",color=0x61FBFB)
	embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
	await ctx.send(embed=embed)

#Help

@client.command()
async def help(ctx):
	embed = discord.Embed(title="CodeHub | Help",description="CodeHub is a bot the helps you learn **Code**.\nCodeHub is open-source.",color=0x61FBFB)
	embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
	embed.add_field(name="\n**Commands**", value="Here Are The Commands!\n\n", inline=False)
	embed.add_field(name="\nDocs", value="**Usage:**\n!docs <Python Docs Name( Example : functions )>\n\n", inline=False)
	embed.add_field(name="Ping", value="**Usage:**\n!ping\n\n", inline=False)
	embed.add_field(name="Binary", value="**Usage:**\n!binary <Text>\n\n", inline=False)
	embed.add_field(name="Debinary", value="**Usage:**\n!debinary <Binary Code>\n\n", inline=False)
	embed.add_field(name="Color", value="**Usage:**\n!color <Color Name>\n\n", inline=False)
	embed.add_field(name="\n\nThe END", value="**Thank you.**\nThe bot has not much commands but later it will improove and will be launched to Everyone on discord!\n\n", inline=False)
	await ctx.send(embed=embed)

#Calculator [V2 (cause the last version did not save)]


#Calculator hydras version

@client.command()
async def calculator(ctx,arg1,arg2,arg3): #arg1 = first num, arg2=symbol, arg3 = second num
  try:
    if arg2 == "+":
      result = int(arg1) + int(arg3)
    if arg2 == "*" or arg2 == "x":
      result = int(arg1) * int(arg3)
    if arg2 == "/" or arg2 == ":":
      result = int(arg1) / int(arg3)
    if arg2 == "-":
      result = int(arg1) - int(arg3)
  
  except ZeroDivisionError as e:
    result = e

  except Exception:
    print(":warning: The operation could not be made or CodeHub messed up")
  
  #result = arg1,arg2,arg3
  await ctx.send(result)


#Binary [ Testing ]

@client.command()
async def binarysometext(ctx):
	embed = discord.Embed(title="CodeHub | Binary",description="0000010100001101111110101010012010010101011",color=0x61FBFB)
	embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
	await ctx.send(embed=embed)

#Debinary [ Testing ]

@client.command()
async def debinary0000010100001101111110101010012010010101011(ctx):
	embed = discord.Embed(title="CodeHub | Debinary",description="some text",color=0x61FBFB)
	embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
	await ctx.send(embed=embed)

	#color [ Testing ]

@client.command()
async def colorblue(ctx):
	embed=discord.Embed(title="CodeHub | Color", url="https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/8/1/1375354802439/Blue---the-colour-008.jpg?width=300&quality=45&auto=format&fit=max&dpr=2&s=d32b70ddf7ecff3771c2d99d32eae422", color=0x00fffb)
	embed.set_thumbnail(url="https://i.guim.co.uk/img/static/sys-images/Guardian/Pix/pictures/2013/8/1/1375354802439/Blue---the-colour-008.jpg?width=300&quality=45&auto=format&fit=max&dpr=2&s=d32b70ddf7ecff3771c2d99d32eae422")
	embed.add_field(name="RGB", value="0, 0, 255", inline=True)
	embed.add_field(name="Hex", value="0000FF", inline=True)
	embed.add_field(name="Name", value="Strong Blue", inline=False)
	embed.set_footer(text=f"Information requested by {ctx.author.display_name}",icon_url=f"{ctx.author.avatar_url}")
	await ctx.send(embed=embed)

#Status Change

@tasks.loop(seconds=3)
async def change_status():
	await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

#Start

keep_alive()
client.run(token)