import discord
from discord.ext import commands, tasks
from discord.ui import *
from itertools import cycle
from discord.commands import Option
from discord import utils
from discord.commands import SlashCommandGroup
import datetime
from googlesearch import search 
import beautifulsoup4
from datetime import datetime, timedelta
import random
import asyncio
import json
import os
from typing import List


bot = commands.Bot(command_prefix='~', 
                   help_command=None, 
                   intents = discord.Intents.all(), 
                   status=discord.Status.idle, 
                   owner_id=734641452214124674,
                  )
for filename in os.listdir("./cogs"):# for every file in a folder in cogs
    if filename.endswith('.py'): #if the file is a python file and if the file is a cog
        bot.load_extension(f'cogs.{filename[:-3]}')#load the extension"

statuses = cycle(["With the API", "Suggest with /suggest!", "/help", "pycord", "With discord imput forms", "New game commands! /help game"])

@tasks.loop(seconds=5.0)
async def status_change():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=next(statuses)))
    
    

help = SlashCommandGroup(name="help", description="help", guild_ids=[918748880705839105])      

class helpcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @help.command()
    async def moderation(ctx):
        e1 = discord.Embed(title="Moderation", description="Below are the Mod commands:\n `clear`, `kick`, `ban`, `unban`, `mute`, `unmute`, `membercount`,`poll`,`warnuser`,`unwarn`,`warnings`,`mod`")
    
        await ctx.respond(embed=e1)
    
    @help.command()
    async def fun(ctx):
    
        e2 = discord.Embed(title="Fun commands", description="Below are the Fun commands:\n `eightball`, `hotcalc`")
    
        await ctx.respond(embed=e2)
        
    @help.command()
    async def utlis(ctx):
    
        e2 = discord.Embed(title="Util commands", description="Below are the util commands:\n `suggest`, `serverinfo`,`userinfo`")
    
        await ctx.respond(embed=e2)
        
    @help.command()
    async def image(ctx):
    
        e2 = discord.Embed(title="Image commands: prefixed", description="Below are the image commands:\n `pixel`,`meme`,`tweet`,`triggered`,`wasted`,`angel`,`hitler`,`delete`,`wanted`,`jail`,`trash`,`discord`")
    
        await ctx.respond(embed=e2)


    bot.add_application_command(help)   


@bot.event
async def on_ready():
    await status_change.start()
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="BYRAMID"))
    print(f'Currently at {len(bot.guilds)} servers!')
    print('Servers connected to:')
    print('')
    for server in bot.guilds:
        print(server.name)
    

    
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
    

@bot.slash_command(guild_ids=[918748880705839105])
@commands.has_permissions(kick_members = True)
async def warnuser(ctx, member: Option(discord.Member, "Member"), reason: Option(str, "reason")):
    await open_account(member)

    users = await get_user_data()

    warns = await warn(member)

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

async def warn(user, change = 1, mode = "warns"):
    users = await get_user_data()

    users[str(user.id)][mode] += change

    with open("./reports.json","w")as f:
        json.dump(users, f)
    
    warns = users[str(user.id)][mode]

    return warns
    

@bot.command()
async def find(ctx,*, query):
    author = ctx.author.mention
    await ctx.channel.send(f"Here are the links related to your question {author} !")
    async with ctx.typing():
        for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
            await ctx.send(f"\n:point_right: {j}")
        await ctx.send("Have any more questions:question:\nFeel free to ask again :smiley: !")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
