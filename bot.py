# -*- coding: utf-8 -*-

"""
bot.py - Init stuff + .version + users logged in status
"""

# Libs
import asyncio
import discord
from discord.ext import commands

from config import config

__author__ = 'JDTech'
__version__ = '0.1.0'


# Default enabled cogs
initial_cogs = ['cogs.admin', 'cogs.tools']


# Bot stuff
TOKEN = config['bot_token']
bot = commands.Bot(command_prefix=config['bot_prefix'])


# Disallow calling the bot in PMs
# TODO: Suppress CheckFailure exceptions
@bot.check
async def no_pm(ctx):
    if ctx.message.guild is None:
        embed = discord.Embed(title="Not allowed to use this command in PMs.", colour=discord.Colour(0xd0021b))
        await ctx.channel.send(embed=embed)
        return False
    else:
        return True


# Reply to mentions
@bot.event
async def on_message(message):
    if message.content == '<@!662158675275808768>':
        embed = discord.Embed(title="Hi there! Do `/help` to see what I can do for ya :smile:", colour=discord.Colour(0x7ed321))
        await message.channel.send(embed=embed)
    else:
        await bot.process_commands(message)


# .version
@bot.command()
async def version(ctx):
    embed = discord.Embed(title=f"*The Tracker*  **v{__version__}**", colour=discord.Colour(0xf8e71c))
    await ctx.send(embed=embed)


# Playing... animation
async def presence_animation():
    while True:
        await bot.change_presence(activity=discord.Game(f'Tracker | {"?"} videos archived'))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Game(f'/help | ~ made by {__author__} ~'))
        await asyncio.sleep(30)


# Print some info
@bot.event
async def on_ready():
    print('---------------')
    print('Connected. Loading cogs...')
    print('---------------')

    # Try to load initial cogs
    for cog in initial_cogs:
        try:
            bot.load_extension(cog)
        except Exception as e:
            print(f'Failed to load extension {cog}. {e}')
        else:
            print(f'Loaded extension {cog}.')

    print('---------------')
    print('Logged in as: ')
    print(f'Username: {bot.user.name} | ID: {bot.user.id}')
    print(f'Discord version: {discord.__version__}')
    print(f'Bot version: {__version__}')
    print('---------------')

    bot.loop.create_task(presence_animation())


if __name__ == "__main__":
    # Run the bot!
    bot.run(TOKEN)
