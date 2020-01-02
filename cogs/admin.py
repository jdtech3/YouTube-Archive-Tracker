# -*- coding: utf-8 -*-

"""
admin.py - includes .load, .unload, .reload

Used to load/reload a cog
"""

# Libs
import discord
from discord.ext import commands


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # .load
    @commands.command(name='load')
    @commands.is_owner()
    async def load_cog(self, ctx, cog: str = None):
        if cog is not None:
            # Try to load the cog, outputting error message if it fails.
            try:
                self.bot.load_extension(cog)
            except Exception as e:
                embed = discord.Embed(title = f'Failed to load extension {cog}. Error: {e}', colour = discord.Colour(0xd0021b))
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = f'Loaded extension {cog}.', colour = discord.Colour(0x7ed321))
                await ctx.send(embed = embed)

        else:
            embed = discord.Embed(title = "No cog given.", colour = discord.Colour(0xd0021b))
            await ctx.send(embed = embed)

    # .unload
    @commands.command(name='unload')
    @commands.is_owner()
    async def unload_cog(self, ctx, cog: str = None):
        if cog is not None:
            # Try to unload the cog, outputting error message if it fails.
            try:
                self.bot.unload_extension(cog)
            except Exception as e:
                embed = discord.Embed(title = f'Failed to unload extension {cog}. Error: {e}', colour = discord.Colour(0xd0021b))
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = f'Unloaded extension {cog}.', colour = discord.Colour(0x7ed321))
                await ctx.send(embed = embed)

        else:
            embed = discord.Embed(title = "No cog given.", colour = discord.Colour(0xd0021b))
            await ctx.send(embed = embed)

    # .reload
    @commands.command(name='reload')
    @commands.is_owner()
    async def reload_cog(self, ctx, cog: str = None):
        if cog is not None:
            # Try to reload the cog, outputting error message if it fails.
            try:
                self.bot.unload_extension(cog)
                self.bot.load_extension(cog)
            except Exception as e:
                embed = discord.Embed(title = f'Failed to reload extension {cog}. Error: {e}', colour = discord.Colour(0xd0021b))
                await ctx.send(embed = embed)
            else:
                embed = discord.Embed(title = f'Reloaded extension {cog}.', colour = discord.Colour(0x7ed321))
                await ctx.send(embed = embed)

        else:
            embed = discord.Embed(title = "No cog given.", colour = discord.Colour(0xd0021b))
            await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(AdminCog(bot))
