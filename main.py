import discord
from discord.ext import commands, tasks
from discord.ui import *
from itertools import cycle
from discord.commands import Option
from discord import Activity, utils
from discord.commands import SlashCommandGroup
import datetime
from datetime import datetime, timedelta
import random
import asyncio
import json
import os
from typing import List



global bot
bot = commands.Bot(command_prefix='~', 
                   help_command=None, 
                   intents = discord.Intents.all(), 
                   activity=discord.Game("Starting up..."),
                   status=discord.Status.dnd, 
                   owner_id=734641452214124674,
                  )





for filename in os.listdir("./cogs"):# for every file in a folder in cogs
    if filename.endswith('.py'): #if the file is a python file and if the file is a cog
        bot.load_extension(f'cogs.{filename[:-3]}')#load the extension"

# statuses = cycle(["With the API", "Suggest with /suggest!", "/help", "pycord", "With discord imput forms", "Check out my github repo!","/report",])


help = SlashCommandGroup(name="help", description="get information on my commands", guild_ids=[918748880705839105])      

class helpcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @help.command()
    async def moderation(ctx):
        e1 = discord.Embed(title="Moderation", description="Below are the Mod commands:\n `clear`, `kick`, `ban`, `unban`, `mute`, `unmute`, `membercount`,`poll`,`warnuser`,`unwarn`,`warnings`,`mod`")
    
        await ctx.respond(embed=e1)
    
    @help.command()
    async def fun(ctx):
    
        e2 = discord.Embed(title="Fun commands", description="Below are the Fun commands:\n `8ball`, `hotcalc`,`cutecalc`")
    
        await ctx.respond(embed=e2)
        
    @help.command()
    async def utils(ctx):
    
        e2 = discord.Embed(title="Util commands", description="Below are the util commands:\n `suggest`, `serverinfo`,`userinfo`,`report`")
    
        await ctx.respond(embed=e2)
    @help.command()
    async def roles(ctx):
    
        e2 = discord.Embed(title="role commands", description="Below are the role commands:\n `rolesage`, `rolesping`,`rolessuggestion`,`rolesanime`,`rolesindian`,`rolesbot`,`rolesgender`,`rolesgame`")
    
        await ctx.respond(embed=e2)    
    
    @help.command()
    async def games(ctx):
    
        e2 = discord.Embed(title="minigames", description="Below are the minigames:\n `rps`, `roll`")
    
        await ctx.respond(embed=e2)
    

    bot.add_application_command(help)   


@bot.event
async def on_ready():
        await bot.change_presence(
            status=discord.Status.idle, 
            activity=discord.Game(
                name="with baby Yoda",
            )
        )
    

    
@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = bot.get_channel(918755817694576650)
    await channel.send(f"{member.mention} has joined. *Help grow :)*")
    
@bot.event
async def on_member_remove(member):
    guild = member.guild
    channel = bot.get_channel(918755817694576650)
    await channel.send(f"{member.mention} has left. thx for joining...")    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is on coodlown for {:.2f} seconds'.format(error.retry_after)
        await ctx.respond(msg)
    if isinstance(error, commands.MissingPermissions):
        await ctx.respond("You cant do that ;-;")    
        

@bot.event
async def on_guild_join(guild):
    user=await bot.fetch_user("734641452214124674")
    print(user, 'Hello {}!'.format(guild.name))



class Suggest_Modal(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(InputText(label="Suggestion title", placeholder="Suggestion title"))

        self.add_item(InputText(label="Suggestion", placeholder="Suggestion", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title=f"New suggestion: {self.children[0].value}", description=self.children[1].value, color=discord.Color.random())      
        user = 734641452214124674
        member = await bot.fetch_user(user)
        await member.send(embed=embed)
        await interaction.response.send_message("Suggestion sent!")
        
    
@bot.slash_command(guild_ids=[918748880705839105], description="Suggest us a bot, or server feature!")
async def suggest(ctx):
    modal = Suggest_Modal(title="Create a new suggestion")
    await ctx.interaction.response.send_modal(modal)

"""

global sotd_embed
sotd_embed = discord.Embed(title="Voting time", description="Various songs have been nominated. its time to vote!", color=discord.Color.random())

class MyModal(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(InputText(label="Song Name", placeholder="Song name"))

        self.add_item(InputText(label="Song Link", placeholder="Song Link", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        sotd_embed.add_field(name=self.children[0].value, value=self.children[1].value, inline=True)
        
        
        await interaction.response.send_message("Song has been added")


        
@bot.command()
async def sotd(ctx):
    embed=discord.Embed(title="Song of the day: Nomnate some songs!", description="Click the button below to nominate a song")

    class MyView(discord.ui.View):
        @discord.ui.button(label="Nominate a song!", emoji="🙋")
        async def button_callback(self, button, interaction):
            modal = MyModal(title="Enter the song details")
            await interaction.response.send_modal(modal)
    
    
    view = MyView()
    
    msg = await ctx.send(embed=embed, view = view)
     
@bot.command()
async def sotdsend(ctx):
    await ctx.send(embed=sotd_embed)
    
"""
@bot.slash_command(guild_ids=[918748880705839105])
@commands.has_permissions(kick_members = True)
async def warn(ctx, member: Option(discord.Member, "Member"), reason: Option(str, "reason")):
    await open_account(member)

    users = await get_user_data()

    warns = await warn1(member)

    await ctx.respond(f"<@{member.id}> warned with reason: **{reason}**. They now have {warns} warns.")

@bot.slash_command(guild_ids=[918748880705839105])
@commands.has_permissions(kick_members = True)
async def unwarn(ctx, member: Option(discord.Member, "Member"), reason: Option(str, "reason")):
    await open_account(member)

    users = await get_user_data()

    warns = await warn1(member, -1)

    await ctx.respond(f"<@{member.id}> warned with reason: **{reason}**. They now have {warns} warns.")

@bot.slash_command(guild_ids=[918748880705839105])
async def warnings(ctx, member: Option(discord.Member, "Member")):
    await open_account(member)

    users = await get_user_data()

    warns = users[str(member.id)]["warns"]

    await ctx.respond(f"{member.name} has {warns} warns.")     
    

async def open_account(user):
    with open ("./reports.json","r")as f:
        users = json.load(f)
    if str (user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["warns"] = 0
    
    with open("./reports.json","w")as f:
        json.dump(users, f)
        
async def get_user_data():
    with open ("./reports.json","r")as f:
        users = json.load(f)
    return users    

async def warn1(user, change = 1, mode = "warns"):
    users = await get_user_data()

    users[str(user.id)][mode] += change

    with open("./reports.json","w")as f:
        json.dump(users, f)
    
    warns = users[str(user.id)][mode]

    return warns
    


class Report_Modal(Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.add_item(InputText(label="Report title", placeholder="Report title"))

        self.add_item(InputText(label="Report", placeholder="Report", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title=f"New Report: {self.children[0].value}", description=self.children[1].value, color=discord.Color.random())      
        user = 734641452214124674
        member = await bot.fetch_user(user)
        await member.send(embed=embed)
        await interaction.response.send_message("Report sent!")
        
    
@bot.slash_command(guild_ids=[918748880705839105], description="Report a member to betches.py")
async def report(ctx):
    modal = Report_Modal(title="Report a member")
    await ctx.interaction.response.send_modal(modal)











    

#---------------------------------------Intro-----------------------------------------------------------------------
    




class Pronouns(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot # For example, you can use self.bot to retrieve a user or perform other functions in the callback.
        # Alternatively you can use Interaction.client, so you don't need to pass the bot instance.
        # Set the options that will be presented inside the dropdown

        options = [
            discord.SelectOption(label="he/him", description="Take this if you are a male.", emoji="♂️"),
            discord.SelectOption(label="she/her", description="Take this if you are a female", emoji="♀️"),
            discord.SelectOption(label="they/them", description="Other"),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Choose your Gender pronouns",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "he/him":
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(953386730357141575)
            await user.add_roles(role)
            if role not in user.roles:
            # Give the user the role if they don't already have it.
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                # Else, Take the role from the user
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )            

            
        if self.values[0] == "she/her":
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(953386719628128276)
            await user.add_roles(role)

            if role not in user.roles:
            # Give the user the role if they don't already have it.
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                # Else, Take the role from the user
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )           
                
        if self.values[0] == "they/them":
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(953386828914892890)
            await user.add_roles(role)

            if role not in user.roles:
            # Give the user the role if they don't already have it.
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                # Else, Take the role from the user
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )           

class PronounsView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Pronouns(self.bot))


class Age(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot

        options = [
            discord.SelectOption(label="10 - 15", description="Take this if you are in the age group of 10 - 15."),
            discord.SelectOption(label="15 - 18", description="Take this if you are in the age group of 15 - 18."),
            discord.SelectOption(label="18 - 22", description="Take this if you are in the age group of 18 - 22."),
        ]

        super().__init__(
            placeholder="Choose your Age group",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "10 - 15": 
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(919921179769331712)
            await user.add_roles(role)
            if role not in user.roles:
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )            

            
        if self.values[0] == "15 - 18":
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(919921261721833524)
            await user.add_roles(role)

            if role not in user.roles:
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )           
                
        if self.values[0] == "18 - 22":
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(919921343452045352)
            await user.add_roles(role)

            if role not in user.roles:
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )           

class AgeView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

        self.add_item(Age(self.bot))


class Ping(discord.ui.Select):
    def __init__(self, bot):
        self.bot = bot

        options = [
            discord.SelectOption(label="Everytime ping", description="Take this if you want to be pinged on every announcement"),
            discord.SelectOption(label="Now and then ping", description="Take this if you want to be pinged sometimes on an announcement"),
            discord.SelectOption(label="Lesser ping", description="Take this if you want to be pinged very rarely on an announcement"),
        ]

        super().__init__(
            placeholder="Choose your ping frequency",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Everytime ping": 
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(919969168789504011)
            await user.add_roles(role)
            if role not in user.roles:
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )            

            
        if self.values[0] == "Now and then ping":
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(919968883757158431)
            await user.add_roles(role)

            if role not in user.roles:
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )           
                
        if self.values[0] == "Lesser ping":
            guild = bot.get_guild(918748880705839105)
            user = guild.get_member(interaction.user.id)
            role = guild.get_role(919968808700104744)
            await user.add_roles(role)

            if role not in user.roles:
                await user.add_roles(role)
                await interaction.response.send_message(f"🎉 You have been given the role {role.mention}", ephemeral=True)
            else:
                await user.remove_roles(role)
                await interaction.response.send_message(
                    f"❌ The {role.mention} role has been taken from you", ephemeral=True
                )           

class PingView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

        self.add_item(Ping(self.bot))












@bot.event
async def on_member_join(member):
    embed = discord.Embed(title=f"Hey {member.name}!", description=f"Below are the roles to get started!\n**Please go forward only if you are comfortable with this**")
    msg = await member.send(content=f"{member.mention} **You have 15 seconds to select one.** ", embed=embed, view=PronounsView(bot))

    await asyncio.sleep(15)

    await msg.edit(content=f"{member.mention} **You have 15 seconds to select one.** ", view=AgeView(bot), embed=None)

    await asyncio.sleep(15)

    await msg.edit(content=f"{member.mention} **You have 15 seconds to select one.** ", view=PingView(bot), embed=None)

    await asyncio.sleep(15)

    await msg.edit(content=f"{member.mention} You're all set! For more roles like this, go to <#919920530415566848> for color roles, go to <#919614012348579890>\n\n Welcome :grin:", embed=None, view=None)

    
    
    











bot.run("OTIwOTAwMDA2NDE0NzkwNzA3.YbrE9w.a6XuFjXarPG4ab-62DflrS9eFuI")
