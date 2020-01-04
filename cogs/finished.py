# -*- coding: utf-8 -*-

"""
finished.py - Implements /finished & /done
"""

# Libs
import pygsheets
import discord
from discord.ext import commands

class FinishedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # .finished
    @commands.command(name='finished', aliases=['done'])
    async def track_finished(self, ctx, link: str = None):
        pass

def setup(bot):
    bot.add_cog(FinishedCog(bot))
