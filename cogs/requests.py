# -*- coding: utf-8 -*-

"""
requests.py - Implements /request & /fill
"""

# Libs
import discord
from discord.ext import commands


class RequestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # .request
    @commands.command(name='request', aliases=['req'])
    async def new_request(self, ctx, link: str = None):
        pass

    # .fill
    @commands.command(name='fill')
    async def fill_request(self, ctx, link: str = None):
        pass


def setup(bot):
    bot.add_cog(RequestCog(bot))
