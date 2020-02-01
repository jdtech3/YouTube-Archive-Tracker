# -*- coding: utf-8 -*-

"""
tools.py - Implements /view & /check
"""

# Libs
import discord
from discord.ext import commands

import requests                     # for link -> API key
from bs4 import BeautifulSoup
from datetime import datetime       # for embed timestamps

import sheets.crud


class ToolsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Get channel ID from link
    def find_chan_id(self, link: str = None):
        if link is not None:
            if link[-1] == '/':
                link += 'videos'
            else:
                link += '/videos'

            resp = requests.get(f"{link}/videos")
            soup = BeautifulSoup(resp.text, features='html.parser')

            chan_id = soup.find('meta', {'itemprop': 'channelId'})['content']
            return chan_id

        else:
            raise TypeError('Link parameter empty')

    # .view / .check
    @commands.command(name='view', aliases=['check'])
    async def view_chan_info(self, ctx, link: str = None):
        if link is not None:
            records = sheets.crud.read(channel_id=self.find_chan_id(link=link))
            for chan in records:
                embed = discord.Embed(title=chan.name, colour=discord.Colour(0x7ed321), url=chan.link, timestamp=datetime.now())

                embed.set_footer(text="The Tracker", icon_url="https://cdn.discordapp.com/avatars/662158675275808768/d01a9cca20797ad7c1b9b5a631b96029.png?size=128")

                embed.add_field(name="Channel ID", value=chan.id, inline=False)

                # Grab the mention (if possible)
                uploader = discord.utils.get(ctx.guild.members, name=chan.uploader.split('#')[0], discriminator=chan.uploader.split('#')[1])
                embed.add_field(name="Channel Archiver", value=uploader.mention if uploader else chan.uploader, inline=False)

                embed.add_field(name="Total Videos", value=f'{chan.total_videos} *(as of {chan.total_videos_date.strftime("%Y-%m-%d") if chan.total_videos_date != "Unknown" else chan.total_videos_date})*')
                embed.add_field(name="Total Videos Archived", value=chan.uploaded_videos)
                embed.add_field(name="Total Archive Size (GB)", value=chan.size_GB)

                # Questionable 1-liner yet again... screw PEP-8 xD
                embed.add_field(name="Last Update", value=chan.last_update_date.strftime('%Y-%m-%d') if chan.last_update_date != "Unknown" else chan.last_update_date)

                embed.add_field(name="Archival Status", value=chan.status)
                embed.add_field(name="Description", value=chan.description)
                embed.add_field(name="Notes", value=chan.notes)
                embed.add_field(name="Channel Language", value=chan.language)
                embed.add_field(name="Uploader Email", value=f'`{chan.uploader_email}`')

                await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title = "No channel link given. Usage: `/view <channel link>`", colour = discord.Colour(0xd0021b))
            await ctx.send(embed = embed)

    # .totalvids / .totalvideos
    @commands.command(name='totalvideos', aliases=['totalvids'])
    async def total_videos(self, ctx, link: str = None):
        chan_id = self.find_chan_id(link=link)
        url = f'https://www.youtube.com/playlist?list={chan_id.replace("UC","UU")}'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, features='html.parser')

        chan_name = soup.select_one('#c4-primary-header-contents > div > div > div:nth-child(1) > h1 > span > span > span > a').string
        video_count = soup.select_one('#pl-header > div.pl-header-content > ul > li:nth-child(2)').string.replace(' videos','')

        embed = discord.Embed(title=f"{chan_name} has `{video_count}` videos.", colour=discord.Colour(0x7ed321))
        await ctx.send(embed=embed)

    # .id
    @commands.command(aliases=['id'])
    async def chan_id(self, ctx, link: str = None):
        chan_id = self.find_chan_id(link=link)
        embed = discord.Embed(title=f"ID: `{chan_id}`", colour=discord.Colour(0x7ed321))
        await ctx.send(embed=embed)

    # .id_batch
    @commands.command(aliases=['id_batch'])
    async def chan_id_batch(self, ctx, pastebin_id: str = None):
        # TODO: Seems to be skipping the first link for whatever reason * NEED TO FIX

        embed = discord.Embed(title=f"Processing...", colour=discord.Colour(0xf8e71c))
        msg = await ctx.send(embed=embed)

        pastebin_url = f'https://pastebin.com/raw/{pastebin_id}'
        # Pass a user-agent so Pastebin doesn't think we're a bot
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'
        resp = requests.get(pastebin_url, headers={'User-Agent': ua})

        if resp.text != 'Error with this ID!':
            # Preprocessing (replace the "carriage returns" and random trailing spaces)
            links = resp.text.split('\n')
            links = [link.replace('\r', '').replace(' ', '') for link in links]

            ids = []
            processed = 0
            for link in links:
                # Status updates
                embed = discord.Embed(title=f"Processed: `{processed}` out of `{len(links)}`", colour=discord.Colour(0xf8e71c))
                await msg.edit(embed=embed)

                # Get chan ID and add to list
                chan_id = self.find_chan_id(link=link)
                ids.append(chan_id)

                processed += 1

            # TODO: Implement message splitting
            # Without message splitting, current limit is about 80 links or so
            ids_str = '\n'.join(ids)
            embed = discord.Embed(title=f"IDs:", description=f"```{ids_str}```", colour=discord.Colour(0x7ed321))
            await ctx.send(embed=embed)

            await msg.delete()      # delete the status message

        else:
            embed = discord.Embed(title=f'Invalid Pastebin ID :confused:', colour=discord.Colour(0xd0021b))
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ToolsCog(bot))
