import discord
from discord.ext import commands
from discord.ui import *
from discord.commands import Option
from discord import utils
from discord.commands import SlashCommandGroup
import datetime
from datetime import datetime, timedelta
import random
import asyncio
from googlesearch import search 
import beautifulsoup4
import json
from typing import List
from discord.commands import slash_command

class Google(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(aliases=['gs', 'google'])
    async def googlesearch(self, ctx,*, query):
        author = ctx.author.mention
        await ctx.channel.send(f"Here are the links related to your question {author} !")
        async with ctx.typing():
            for j in search(query, tld="co.in", num=3, stop=3, pause=2): 
                await ctx.send(f"\n:point_right: {j}")
            await ctx.send("Have any more questions:question:\nFeel free to ask again :smiley: !")
def setup(bot):
    bot.add_cog(google(bot))
