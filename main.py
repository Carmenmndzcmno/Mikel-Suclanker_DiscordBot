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
load_dotenv() #this will load the current environment variable file
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(Filename='discord.log', encoding='utf-8', mode='w') #mode w -> write mode

#Intents are the actions that our bot will respond
intents = discord.Intents.default()
intents.message_content = True # we specify that the bot wants to receive the message content of the user's messages
intents.members = True # the bot can respond different events around the discord users
# As we expand the bot, we will be setting more variables to true.
# All existent intents: https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents

bot = commands.Bot(command_prefix='!', intents=intents) # We wrote down de command prefix up to the bot