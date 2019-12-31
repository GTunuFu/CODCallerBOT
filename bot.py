import discord
import asyncio
from discord.ext import commands #bringing in discord commands from discord extension


client = commands.Bot(command_prefix = '.')

@client.event #these events are basically funtions but easier to label them functions
async def on_ready(): #when function is ready to run
# common first event to run
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

client.run('NjYwOTgyMDQwOTk2MzQ3OTE3.XglhoQ.mcntpWJX6YhfhYdyuCwCrJ4YUGc') #taken token from discord dev portal
