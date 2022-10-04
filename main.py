#No touch above
from better_profanity import profanity
from discord.ext import commands
import os,discord,tools
profanity.load_censor_words_from_file("./storage/profanity.txt")
intents = discord.Intents.all() # Imports all the Intents
intents.members=True
client = commands.Bot(command_prefix="->",intents=intents)

@client.event
async def on_ready():
  print("Ready")

@client.command()
async def ping(ctx):
  await ctx.send('Pong, {} Ms'.format(round(client.latency * 1000,2)))

@client.command()
async def getavatar(ctx, target:discord.Member):
  
  await ctx.channel.send(target.avatar_url)


token=os.getenv("TOKEN")    
client.run(token)