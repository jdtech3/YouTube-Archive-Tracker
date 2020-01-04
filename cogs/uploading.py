# -*- coding: utf-8 -*-

"""
uploading.py - Implements /uploading & /ul
"""

# Libs
import pygsheets
import discord
from discord.ext import commands

class UploadCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # .downloading
    @commands.command(name='uploading', aliases=['ul'])
    async def track_upload(self, ctx, link: str = None):
        pass

def setup(bot):
    bot.add_cog(UploadCog(bot))
