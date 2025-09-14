import discord #Imports the library discord.py
from discord.ext import commands
import logging
from dotenv import load_dotenv #allows us to load environment variable files
import os

"""
       _____  .___ __          .__    _________                    .__                 __                 
   *                       (                                                        
 (  `           )       (  )\ )                    (                  )             
 )\))(   (   ( /(    (  )\(()/(   (      )         )\    )         ( /(    (   (    
((_)()\  )\  )\())  ))\((_)/(_)) ))\    (      (  ((_)( /(   (     )\())  ))\  )(   
(_()((_)((_)((_)\  /((_)_ (_))  /((_)   )\  '  )\  _  )(_))  )\ ) ((_)\  /((_)(()\  
|  \/  | (_)| |(_)(_)) | |/ __|(_))(  _((_))  ((_)| |((_)_  _(_/( | |(_)(_))   ((_) 
| |\/| | | || / / / -_)| |\__ \| || || '  \()/ _| | |/ _` || ' \))| / / / -_) | '_| 
|_|  |_| |_||_\_\ \___||_||___/ \_,_||_|_|_| \__| |_|\__,_||_||_| |_\_\ \___| |_|   
      
    Developers:                                                                              
        Mendez Camino, Carmen
        Rodriguez Bilbao, Nicolas
    
    References: https://discordpy.readthedocs.io/en/stable
        -> Modern Pythonic API using async/await syntax
        
    Prerequisites:
        -> Python 3.8 or higher
        
    Before We Start Coding [Applied for Windows 10/11 users]:
        Get the library directly from PyPI: py -3 -m pip install -U discord.py
        To get voice support, you should use discord.py[voice] instead of discord.py, e.g.: python3 -m pip install -U discord.py[voice]
        Install python-dotenv: pip install python-dotenv

        VIRTUAL ENVIROMENTS!!!
            $ cd your-bot-source
            $ python3 -m venv bot-env
            $ bot-env\Scripts\activate.bat
            $ pip install -U discord.py

    Basic Concepts: discord.py follows an event-oriented programming paradigm

""" 
load_dotenv() # this will load the current environment variable file
token = os.getenv('DISCORD_TOKEN')

# Set up logging
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') # mode w -> write mode 
logging.basicConfig(level=logging.INFO, handlers=[handler]) # mode w -> write mode

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