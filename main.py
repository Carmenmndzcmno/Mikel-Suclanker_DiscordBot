import discord #Imports the library discord.py
from discord.ext import commands
import logging
from dotenv import load_dotenv #allows us to load environment variable files
import os

"""
      mikelsumclanker   
      
    Developers:                                                                              
        Mendez Camino, Carmen
        Rodriguez Bilbao, Nicolas
    
    References: https://discordpy.readthedocs.io/en/stable
        -> Modern Pythonic API using async/await syntax
        
    

""" 
load_dotenv() # this will load the current environment variable file
token = os.getenv('DISCORD_TOKEN')

# Set up logging
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w') # mode w -> write mode 
logging.basicConfig(level=logging.DEBUG, handlers=[handler]) # mode w -> write mode

# Intents specify which events the bot will receive
intents = discord.Intents.default()
intents.message_content = True # receive the content of user messages
intents.members = True # respond to events related to server members
# As we expand the bot, we will be setting more variables to true.
# All existent intents: https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents) # set command prefix and intents

# Handling Events
@bot.event
async def on_ready(): # is the bot ready?
    print(f"bipbaraberobop, {bot.user.name}")
    #logging.info(f"Bot connected as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_member_join(member): # did someone join the discord server?
    await member.send(f"¡Bienvenido, {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user: return

bot.run(token)