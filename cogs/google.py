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

class Modal(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(InputText(label="Search query", placeholder="Search query"))


    async def callback(self, interaction: discord.Interaction):
    	embed = discord.Embed(title=f"New google search results", description=f"search query: {self.children[0].value}", color=discord.Color.random())      
    	for j in search(self.children[0].value, num=1, stop=1, pause=2): 
    		embed.add_field(name=j, value="google search query")

        
        await interaction.response.send_message(embed=embed)

class google(commands.Cog):
	def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[918748880705839105])
    async def googlesearch(ctx):
    	modal = Modal(title="Google search")
        await ctx.interaction.response.send_modal(modal)

def setup(bot):
    bot.add_cog(google(bot))
