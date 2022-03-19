import discord
from discord.ext import commands
from discord.utils import get
from main import bot


#-------------------------------Pronouns--------------------------------------

class Pronouns(discord.ui.Select):
    def __init__(self):
        self.bot = bot # For example, you can use self.bot to retrieve a user or perform other functions in the callback.
        # Alternatively you can use Interaction.client, so you don't need to pass the bot instance.
        # Set the options that will be presented inside the dropdown

        options = [
            discord.SelectOption(label="he/him", description="Take this if you are a male.", emoji="🟥"),
            discord.SelectOption(label="she/her", description="Take this if you are a female", emoji="🟩"),
            discord.SelectOption(label="they/them", description="Other", emoji="🟦"),
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
        role = discord.utils.get(guild.roles,name=self.values[0])
        member = discord.Interaction.user
        await member.add_roles(role)

class PronounsView(discord.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Pronouns(self.bot))




class Intro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(member):
        view = PronounsView(bot)
        await member.send("Gender roles:", view=view)

def setup(bot):
    bot.add_cog(Intro(bot))
    