# -*- coding: utf-8 -*-

"""
help.py - Implements /help
"""

# Libs
import discord
from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')

    # /help
    @commands.group()
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("""```css
[ Command List ]

- Use /help [command] for details -

/view         :: Query records for a channel
/id           :: Channel ID of a channel
/totalvideos  :: Total videos of a channel
-
/load         :: [ADMIN] Load internal cogs
/unload       :: [ADMIN] Unload internal cogs
/reload       :: [ADMIN] Reload internal cogs
```
""")

    # /help view
    @help.command(aliases=['check'])
    async def view(self, ctx):
        await ctx.send("""
```css
[ View / Check Records ]

Returns records for a channel (pulls from index spreadsheet). If no records are found, the bot will not reply.

Usage: /view  <channel link>
       /check <channel link>
```
""")

    # /help id
    @help.command(aliases=['id'])
    async def chan_id(self, ctx):
        await ctx.send("""
```css
[ Get Channel ID ]

Returns channel ID of a channel given channel/video link.

Usage: /id      <channel link>
       /chan_id <channel link>
```
""")

    # /help totalvideos
    @help.command(aliases=['totalvids'])
    async def totalvideos(self, ctx):
        await ctx.send("""
```css
[ Get Total Videos of Channel ]

Returns total video count of a particular channel.

Usage: /totalvids   <channel link>
       /totalvideos <channel link>
```
""")


def setup(bot):
    bot.add_cog(HelpCog(bot))
