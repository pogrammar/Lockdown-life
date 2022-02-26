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
import json
from typing import List
from discord.commands import slash_command

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[918748880705839105])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount: Option(int, "Member")):
        await ctx.channel.purge(limit = amount)
        await ctx.respond("Done.")


    @slash_command(guild_ids=[918748880705839105])
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx,  member: Option(discord.Member, "Member")):

        await member.kick(reason=None)
        await ctx.respond("Done.")


    @slash_command(guild_ids=[918748880705839105])
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: Option(discord.Member, "Member")):

        await member.ban(reason=None, delete_message_days=0)
        await ctx.respond("Done.")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, member : discord.Member):

        await member.unban(member, reason=None)
        await ctx.respond("Done.")


    @slash_command(guild_ids=[918748880705839105])
    @commands.has_permissions(manage_roles = True)
    async def mute(self, ctx, member: Option(discord.Member, "Member")):
        muted_role = ctx.guild.get_role(919600309817462785)

        await member.add_roles(muted_role)

        await ctx.respond("The member has been muted")


    @slash_command(guild_ids=[918748880705839105])
    @commands.has_permissions(manage_roles = True)
    async def unmute(self, ctx, member: Option(discord.Member, "Member")):
        muted_role = ctx.guild.get_role(919600309817462785)

        await member.remove_roles(muted_role)

        await ctx.respond("The member has been unmuted")


    @slash_command(guild_ids=[918748880705839105])
    async def membercount(self, ctx):
        await ctx.respond(ctx.guild.member_count)


    @slash_command(guild_ids=[918748880705839105])
    async def poll(self, ctx, question: Option(str, "Question"), a: Option(str, "Option 1"), b: Option(str, "Option 2")):

        embed = discord.Embed(title=question, description=f"<:a_:920520686227845230>: {a}\n <:b_:920520686278172742>: {b}")
        await ctx.respond(embed=embed)
        msg = await ctx.interaction.original_message()
        await msg.add_reaction('<:a_:920520686227845230>')
        await msg.add_reaction('<:b_:920520686278172742>')
        
    
    @slash_command(guild_ids=[918748880705839105], description="get deh mod app")
    async def mod(self, ctx):
        await ctx.respond("Mod application: https://forms.gle/XFgGRdoeTeYsD4Fk6")
    

def setup(bot):
    bot.add_cog(Moderation(bot))