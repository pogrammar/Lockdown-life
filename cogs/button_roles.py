import discord
from discord.commands.core import slash_command
from discord.ext import commands

#--------------------------------------------AGE ROLES---------------------------------------------------------------------------
age_role_ids = [919921179769331712, 919921261721833524, 919921343452045352]
class RoleButtonAge(discord.ui.Button):
    def __init__(self, role: discord.Role):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=role.name,
            style=discord.enums.ButtonStyle.primary,
            custom_id=str(role.id),
        )

    async def callback(self, interaction: discord.Interaction):
        """This function will be called any time a user clicks on this button.
        Parameters
        ----------
        interaction : discord.Interaction
            The interaction object that was created when a user clicks on a button.
        """
        # Figure out who clicked the button.
        user = interaction.user
        # Get the role this button is for (stored in the custom ID).
        role = interaction.guild.get_role(int(self.custom_id))

        if role is None:
            # If the specified role does not exist, return nothing.
            # Error handling could be done here.
            return

        # Add the role and send a response to the uesr ephemerally (hidden to other users).
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



#--------------------------------------------Ping Roles---------------------------------------------------------------------------
 
ping_role_ids = [919969168789504011, 919968883757158431, 919968808700104744]
class RoleButtonPing(discord.ui.Button):
    def __init__(self, role: discord.Role):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=role.name,
            style=discord.enums.ButtonStyle.primary,
            custom_id=str(role.id),
        )

    async def callback(self, interaction: discord.Interaction):
        """This function will be called any time a user clicks on this button.
        Parameters
        ----------
        interaction : discord.Interaction
            The interaction object that was created when a user clicks on a button.
        """
        # Figure out who clicked the button.
        user = interaction.user
        # Get the role this button is for (stored in the custom ID).
        role = interaction.guild.get_role(int(self.custom_id))

        if role is None:
            # If the specified role does not exist, return nothing.
            # Error handling could be done here.
            return

        # Add the role and send a response to the uesr ephemerally (hidden to other users).
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

#--------------------------------------------Suggestion Roles---------------------------------------------------------------------------
 
suggestion_role_ids = [919969168789504011, 919968883757158431, 919968808700104744]
class RoleButtonSuggestion(discord.ui.Button):
    def __init__(self, role: discord.Role):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=role.name,
            style=discord.enums.ButtonStyle.primary,
            custom_id=str(role.id),
        )

    async def callback(self, interaction: discord.Interaction):
        """This function will be called any time a user clicks on this button.
        Parameters
        ----------
        interaction : discord.Interaction
            The interaction object that was created when a user clicks on a button.
        """
        # Figure out who clicked the button.
        user = interaction.user
        # Get the role this button is for (stored in the custom ID).
        role = interaction.guild.get_role(int(self.custom_id))

        if role is None:
            # If the specified role does not exist, return nothing.
            # Error handling could be done here.
            return

        # Add the role and send a response to the uesr ephemerally (hidden to other users).
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



#--------------------------------------------Anime Roles---------------------------------------------------------------------------
 
anime_role_ids = [929615457609191473]
class RoleButtonAnime(discord.ui.Button):
    def __init__(self, role: discord.Role):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=role.name,
            style=discord.enums.ButtonStyle.primary,
            custom_id=str(role.id),
        )

    async def callback(self, interaction: discord.Interaction):
        """This function will be called any time a user clicks on this button.
        Parameters
        ----------
        interaction : discord.Interaction
            The interaction object that was created when a user clicks on a button.
        """
        # Figure out who clicked the button.
        user = interaction.user
        # Get the role this button is for (stored in the custom ID).
        role = interaction.guild.get_role(int(self.custom_id))

        if role is None:
            # If the specified role does not exist, return nothing.
            # Error handling could be done here.
            return

        # Add the role and send a response to the uesr ephemerally (hidden to other users).
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

#--------------------------------------------indian Roles---------------------------------------------------------------------------
 
indian_role_ids = [931778093977313320]
class RoleButtonIndian(discord.ui.Button):
    def __init__(self, role: discord.Role):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=role.name,
            style=discord.enums.ButtonStyle.primary,
            custom_id=str(role.id),
        )

    async def callback(self, interaction: discord.Interaction):
        """This function will be called any time a user clicks on this button.
        Parameters
        ----------
        interaction : discord.Interaction
            The interaction object that was created when a user clicks on a button.
        """
        # Figure out who clicked the button.
        user = interaction.user
        # Get the role this button is for (stored in the custom ID).
        role = interaction.guild.get_role(int(self.custom_id))

        if role is None:
            # If the specified role does not exist, return nothing.
            # Error handling could be done here.
            return

        # Add the role and send a response to the uesr ephemerally (hidden to other users).
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


#--------------------------------------------Bot Roles---------------------------------------------------------------------------
 
bot_role_ids = [945965479816744961]
class RoleButtonBot(discord.ui.Button):
    def __init__(self, role: discord.Role):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=role.name,
            style=discord.enums.ButtonStyle.primary,
            custom_id=str(role.id),
        )

    async def callback(self, interaction: discord.Interaction):
        """This function will be called any time a user clicks on this button.
        Parameters
        ----------
        interaction : discord.Interaction
            The interaction object that was created when a user clicks on a button.
        """
        # Figure out who clicked the button.
        user = interaction.user
        # Get the role this button is for (stored in the custom ID).
        role = interaction.guild.get_role(int(self.custom_id))

        if role is None:
            # If the specified role does not exist, return nothing.
            # Error handling could be done here.
            return

        # Add the role and send a response to the uesr ephemerally (hidden to other users).
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

#--------------------------------------------Gender Roles---------------------------------------------------------------------------
 
gender_role_ids = [953386730357141575, 953386719628128276, 953386828914892890]
class RoleButtonGender(discord.ui.Button):
    def __init__(self, role: discord.Role):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=role.name,
            style=discord.enums.ButtonStyle.primary,
            custom_id=str(role.id),
        )

    async def callback(self, interaction: discord.Interaction):
        """This function will be called any time a user clicks on this button.
        Parameters
        ----------
        interaction : discord.Interaction
            The interaction object that was created when a user clicks on a button.
        """
        # Figure out who clicked the button.
        user = interaction.user
        # Get the role this button is for (stored in the custom ID).
        role = interaction.guild.get_role(int(self.custom_id))

        if role is None:
            # If the specified role does not exist, return nothing.
            # Error handling could be done here.
            return

        # Add the role and send a response to the uesr ephemerally (hidden to other users).
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




















class ButtonRoleCog(commands.Cog):
    """A cog with a slash command for posting the message with buttons
    and to initialize the view again when the bot is restarted.
    """

    def __init__(self, bot):
        self.bot = bot

    # Make sure to provide a list of guild ids in the guild_ids kwarg argument.
    @slash_command(guild_ids=[918748880705839105], description="Get the age roles")
    async def rolesage(self, ctx: commands.Context):
        """Slash command to post a new view with a button for each role."""

        embed = discord.Embed(title="Choose your age", description="<@&953386730357141575>\n<@&953386719628128276>\n<@&953386828914892890>")

        # timeout is None because we want this view to be persistent.
        view = discord.ui.View(timeout=None)

        # Loop through the list of roles and add a new button to the view for each role.
        for role_id in age_role_ids:
            # Get the role from the guild by ID.
            role = ctx.guild.get_role(role_id)
            view.add_item(RoleButtonAge(role))

        await ctx.respond(embed=embed, view=view)

    @slash_command(guild_ids=[918748880705839105], description="Get the gender roles")
    async def rolesgender(self, ctx: commands.Context):
        embed = discord.Embed(title="Choose your gender", description="<@&919969168789504011>\n<@&919968883757158431>\n<@&919968808700104744>")

        view = discord.ui.View(timeout=None)


        for role_id in gender_role_ids:
            role = ctx.guild.get_role(role_id)
            view.add_item(RoleButtonGender(role))

        await ctx.respond(embed=embed, view=view)  


    @slash_command(guild_ids=[918748880705839105], description="Get the ping roles")
    async def rolesping(self, ctx: commands.Context):
        embed = discord.Embed(title="Choose your ping roles", description="<@&953386730357141575>\n<@&953386719628128276>\n<@&953386828914892890>")
        view = discord.ui.View(timeout=None)

        for role_id in ping_role_ids:
            role = ctx.guild.get_role(role_id)
            view.add_item(RoleButtonPing(role))

        await ctx.respond(embed=embed, view=view)

    @slash_command(guild_ids=[918748880705839105], description="Get the suggestion roles")
    async def rolessuggestion(self, ctx: commands.Context):
        """Slash command to post a new view with a button for each role."""

        # timeout is None because we want this view to be persistent.
        view = discord.ui.View(timeout=None)

        # Loop through the list of roles and add a new button to the view for each role.
        for role_id in suggestion_role_ids:
            # Get the role from the guild by ID.
            role = ctx.guild.get_role(role_id)
            view.add_item(RoleButtonSuggestion(role))

        await ctx.respond("Choose your avisory method", view=view) 

    @slash_command(guild_ids=[918748880705839105], description="Get the anime roles")
    async def rolesanime(self, ctx: commands.Context):
        """Slash command to post a new view with a button for each role."""

        # timeout is None because we want this view to be persistent.
        view = discord.ui.View(timeout=None)

        # Loop through the list of roles and add a new button to the view for each role.
        for role_id in anime_role_ids:
            # Get the role from the guild by ID.
            role = ctx.guild.get_role(role_id)
            view.add_item(RoleButtonAnime(role))

        await ctx.respond("Do you like anime? choose this role for anime pings for updates.", view=view)

    @slash_command(guild_ids=[918748880705839105], description="Get the indian roles")
    async def rolesindian(self, ctx: commands.Context):
        """Slash command to post a new view with a button for each role."""

        # timeout is None because we want this view to be persistent.
        view = discord.ui.View(timeout=None)

        # Loop through the list of roles and add a new button to the view for each role.
        for role_id in indian_role_ids:
            # Get the role from the guild by ID.
            role = ctx.guild.get_role(role_id)
            view.add_item(RoleButtonIndian(role))

        await ctx.respond("Are you indian? choose this for festive roles <:pepeHmmm:919825231965720586>", view=view)

    @slash_command(guild_ids=[918748880705839105], description="Get the bot roles")
    async def rolesbot(self, ctx: commands.Context):
        """Slash command to post a new view with a button for each role."""

        # timeout is None because we want this view to be persistent.
        view = discord.ui.View(timeout=None)

        # Loop through the list of roles and add a new button to the view for each role.
        for role_id in bot_role_ids:
            # Get the role from the guild by ID.
            role = ctx.guild.get_role(role_id)
            view.add_item(RoleButtonBot(role))

        await ctx.respond("Dont shout at betches on pings now <:EEEEEEEE:948472349286621286>", view=view)    

    





    @commands.Cog.listener()
    async def on_ready(self):
        """This method is called every time the bot restarts.
        If a view was already created before (with the same custom IDs for buttons)
        it will be loaded and the bot will start watching for button clicks again.
        """
        # We recreate the view as we did in the /post command.
        view = discord.ui.View(timeout=None)
        # Make sure to set the guild ID here to whatever server you want the buttons in!
        guild = self.bot.get_guild(918748880705839105)
        for role_id in ping_role_ids:
            role = guild.get_role(role_id)
            view.add_item(RoleButtonPing(role))
        for role_id in anime_role_ids:
            role = guild.get_role(role_id)
            view.add_item(RoleButtonAnime(role))
        for role_id in indian_role_ids:
            role = guild.get_role(role_id)
            view.add_item(RoleButtonIndian(role))
        for role_id in bot_role_ids:
            role = guild.get_role(role_id)
            view.add_item(RoleButtonBot(role))
        for role_id in age_role_ids:
            role = guild.get_role(role_id)
            view.add_item(RoleButtonAge(role))
        for role_id in suggestion_role_ids:
            role = guild.get_role(role_id)
            view.add_item(RoleButtonSuggestion(role))
        for role_id in gender_role_ids:
            role = guild.get_role(role_id)
            view.add_item(RoleButtonGender(role))

        # Add the view to the bot so it will watch for button interactions.
        self.bot.add_view(view)


def setup(bot):
    bot.add_cog(ButtonRoleCog(bot))