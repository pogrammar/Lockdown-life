import random

import discord
from discord.ext import commands
from discord.commands import Option, slash_command  #Importing the packages
from discord.commands import slash_command


class Fun(commands.Cog):
    def __init__(self, bot):#to Initialise
        self.bot = bot

    @slash_command(guild_ids=[918748880705839105], name="8ball")
    async def eightball(self, ctx, question: Option(str)):
        ballresponse = [
            "Yes", "No", "Take a wild guess...", "Very doubtful",
            "Sure", "Without a doubt", "Most likely", "Might be possible",
            "You'll be the judge", "no... (╯°□°）╯︵ ┻━┻", "no... baka",
            "senpai, pls no ;-;","i think....","gg","I-\ndont know what to say","oh well","My pogramming refuses to answer that question"
        ]

        answer = random.choice(ballresponse)
        await ctx.respond(f"🎱 **Question:** {question}\n**Answer:** {answer}")
    
    @slash_command(guild_ids=[918748880705839105])
    async def hotcalc(self, ctx, user: Option(discord.Member)):    
        r = random.randint(1, 100)
        hot = r / 1.17

        if hot > 75:
            emoji = "💞"
        elif hot > 50:
            emoji = "💖"
        elif hot > 25:
            emoji = "❤"
        else:
            emoji = "💔"    

        await ctx.respond(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")      

    @slash_command(guild_ids=[918748880705839105])
    async def cutecalc(self, ctx, user: Option(discord.Member)):    
        r = random.randint(1, 100)
        cute = r / 1.17

        if cute > 75:
            emoji = "😍"
        elif cute > 50:
            emoji = "😉"
        elif cute > 25:
            emoji = "🥸"
        else:
            emoji = "😶‍🌫️"    

        await ctx.respond(f"**{user.name}** is **{cute:.2f}%** cute {emoji}")            


def setup(bot):
    bot.add_cog(Fun(bot))        
