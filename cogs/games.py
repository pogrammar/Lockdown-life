import discord
from discord.ext import commands
import asyncio
import random
import datetime
from discord.commands import slash_command

class Games(commands.Cog):
    """<:games:819957465160220734> Fun Games to play when bored."""
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rps(self, ctx):
        """Rock Paper Scissors game."""
        try:
            rpsEmbed = discord.Embed(color=random.randint(
                0, 0xffffff))
            rpsEmbed.add_field(name='Rock', value='\U0001faa8')
            rpsEmbed.add_field(name='Paper', value='\U0001f4dc')
            rpsEmbed.add_field(name='Scissors', value='\U00002702')
            rpsEmbed.set_footer(text='the message you will be deleted after 1 min')
            question_choose = await ctx.send(embed=rpsEmbed)
            await question_choose.add_reaction('\U0001faa8')
            await question_choose.add_reaction('\U0001f4dc')
            await question_choose.add_reaction('\U00002702')
            reaction, user = await self.bot.wait_for('reaction_add', check=lambda reaction, user: user == ctx.author and str(reaction.emoji), timeout=60)
            
            selects = [u'\U00002702', u'\U0001faa8', u'\U0001f4dc']
            
            bot_select = random.choice(selects)
            print(str(bot_select))
            
            user_select = str(reaction.emoji)
            print(str(user_select))
        
            if str(user_select) == str(bot_select):
                await question_choose.delete()
                
                if str(bot_select) == u'\U00002702':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='Tie', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
                
                elif str(bot_select) == u'\U0001faa8':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='Tie', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
                
                elif str(bot_select) == u'\U0001f4dc':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='Tie', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/microsoft/209/anticlockwise-downwards-and-upwards-open-circle-arrows_1f504.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
            
            elif str(user_select) == u'\U0001faa8':
                await question_choose.delete()
                if str(bot_select) == u'\U00002702':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Win', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
                elif str(bot_select) == u'\U0001f4dc':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Lose', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
            elif str(user_select) == u'\U0001f4dc':
                await question_choose.delete()
                if str(bot_select) == u'\U0001faa8':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Win', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
                elif str(bot_select) == u'\U00002702':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Lose', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
            elif str(user_select) == u'\U00002702':
                await question_choose.delete()
                if str(bot_select) == u'\U0001faa8':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Lose', icon_url='https://images.emojiterra.com/mozilla/512px/274c.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
                elif str(bot_select) == u'\U0001f4dc':
                    choose_embed = discord.Embed(color=0x2ecc71)
                    choose_embed.add_field(
                        name='User Choose :bust_in_silhouette:', value=f'**{user_select}**', inline=True)
                    choose_embed.add_field(
                        name='Bot Choose :robot:', value=f'**{bot_select}**', inline=True)
                    choose_embed.set_author(
                        name='You Win', icon_url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/check-mark-button_2705.png')
                    choose_embed.set_footer(
                        text=ctx.author.name, icon_url=ctx.author.avatar.url)
                    await ctx.send(embed=choose_embed)
        except asyncio.TimeoutError:
            timeout = await ctx.send('The Time is end try again')
            await timeout.delete(delay=10)

    @commands.command(aliases=['dice'])
    async def roll(self, ctx):
        """Rolls a dice... That's all."""
        message = await ctx.send("Choose a number:\n**4**, **6**, **8**, **10**, **12**, **20** ")
        
        def check(m):
            return m.author == ctx.author

        try:
            message = await self.bot.wait_for("message", check = check, timeout = 30.0)
            m = message.content

            if m != "4" and m != "6" and m != "8" and m != "10" and m != "12" and m != "20":
                await ctx.send("Sorry, invalid choice.")
                return
            
            await ctx.send(f"**{random.randint(1, int(m))}**")
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("Process has been canceled because you didn't respond in **30 seconds**")

def setup(bot):
    bot.add_cog(Games(bot))