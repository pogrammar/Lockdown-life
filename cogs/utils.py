import discord
from discord.ext import commands
from discord.ui import *
from discord.commands import Option, slash_command

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
       

    @slash_command(guild_ids=[918748880705839105])
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
   
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.random()
        )
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.respond(embed=embed)

    @slash_command(guild_ids=[918748880705839105], description="Get a user's unfo")
    async def userinfo(self, ctx, user: Option(discord.Member, "Member")): 
        embed = discord.Embed(title="{}'s info".format(user), color=0x176cd5)
        embed.add_field(name="Username", value=user.name + "#" + user.discriminator, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Roles", value=len(user.roles))
        embed.add_field(name="Joined", value=user.joined_at)
        embed.add_field(name="Created", value=user.created_at)
        embed.add_field(name="Bot?", value=user.bot)
        await ctx.respond(embed=embed)    

def setup(bot):
    bot.add_cog(Utils(bot))