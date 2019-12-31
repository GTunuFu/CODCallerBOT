import discord
import asyncio
import random
from discord.ext import commands #bringing in discord commands from discord extension


client = commands.Bot(command_prefix = '.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event #these events are basically funtions but easier to label them functions
async def on_ready(): #when function is ready to run
# common first event to run
    print('Bot is ready.')

@client.command() #legit just a command
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball','test']) #works as these any of these functions can call for the command
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes - definitely',
                'You may rely on it',
                'As I see it, yes',
                'Most likely',
                'Outlook good',
                'Yes',
                'Signs point to yes',
                'Reply hazy, try again'
                'Ask again later',
                'Better not tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                "Don't count on it",
                'My reply is no',
                'My sources say no',
                'Outlook not so good',
                'Very doubtful']
    await ctx.send(f'Question: {question} \n Answer: {random.choice(responses)}')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

client.run('NjYwOTgyMDQwOTk2MzQ3OTE3.Xgu5Uw.1KXoOfwIRsItslzy2j5NqOfxWlw') #taken token from discord dev portal
