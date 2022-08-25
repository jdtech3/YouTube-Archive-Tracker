# -*- coding: utf-8 -*-

"""
projects.py - Implements /update-projects
"""

# Libs
import asyncio
import discord
from discord.ext import commands, tasks

import sheets.crud_projects


class ProjectsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # .update-projects
    @commands.command(name='update-projects', aliases=['updateprojects'])
    async def update_project_list(self, ctx):
        projects_chan = self.bot.get_channel(1012096820878520413)

        # Find the message
        message = None
        async for msg in projects_chan.history(limit=None):
            if (msg.author == self.bot.user) and (msg.content != '') and (msg.content[0] == '—'):
                message = msg
                break

        # Create message if it doesn't exist
        if message is None:
            message = await projects_chan.send('—')

        # Grab data
        projects = sheets.crud_projects.read()

        # Build and send message
        proj_msgs = []
        for proj in projects:
            # Preprocessing
            chan, contact, contributors, goals, links = None, None, [], None, []

            if proj.name is not None:
                chan = discord.utils.get(projects_chan.guild.channels, name=proj.name)
            chan = chan.mention if chan is not None else f'**{proj.name}**'

            if proj.contact is not None:
                contact = projects_chan.guild.get_member_named(proj.contact)
            contact = contact.mention if contact is not None else '*?*'

            if proj.contributors is not None:
                for name in proj.contributors:
                    c = projects_chan.guild.get_member_named(name)
                    contributors.append(c.mention if c is not None else name)
            contributors = ('\n' + '\n'.join(contributors)) if contributors else '*?*'

            goals = proj.goals if proj.goals is not None else '*?*'

            links = ('\n' + '\n'.join(proj.links)) if proj.links is not None else '*?*'

            proj_msgs.append(
                f'-- {chan} --\n' +
                f'**Project lead/contact person:** {contact}\n' +
                f'**Project contributors:** {contributors}\n' +
                f'**Project goals:** {goals}\n' +
                f'**Code/docs:** {links}\n'
            )

        await message.edit(content='—\n' + '—\n'.join(proj_msgs) + '—', suppress=True)

        # Delete original message
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(ProjectsCog(bot))
