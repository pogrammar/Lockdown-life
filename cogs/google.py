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

    @slash_command(guild_ids=[918748880705839105])
    async def googlesearch(ctx, query: Option(str, "Search query")):
	async with ctx.typing():
            embed = discord.Embed(title="Google search", description="Here are your results:")
	    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
			embed.add_field(name=j, description=f"Result for search query: {query}")
        await ctx.respond(embed=embed) 
def setup(bot):
    bot.add_cog(google(bot))
