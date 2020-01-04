# -*- coding: utf-8 -*-

"""
downloading.py - Implements /dl & /downloading
"""

# Libs
import pygsheets
import discord
from discord.ext import commands

class DownloadCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # .downloading
    @commands.command(name='downloading', aliases=['dl'])
    async def track_download(self, ctx, link: str = None):
        pass

def setup(bot):
    bot.add_cog(DownloadCog(bot))
