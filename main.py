import discord
from discord.ext import commands

# Initialize bot
intents = discord.Intents.default()
intents.message_content = True  # Needed for message commands
intents.members = True  # Allows bot to see members

bot = commands.Bot(command_prefix="/", intents=intents)

# Channel ID restriction
ALLOWED_CHANNEL_ID = 1354227817759510700

# /logitech command
@bot.tree.command(name="logitech")
async def logitech(interaction: discord.Interaction):
    # Check if the command is used in the allowed channel
    if interaction.channel.id != ALLOWED_CHANNEL_ID:
        await interaction.response.send_message("This command can only be used in the designated channel.", ephemeral=True)
        return

    # Message to send to the user
    message = "[**R6 Logitech Recoil Script**](https://www.mediafire.com/folder/ixl8lxszjokth/LOGITECH+RECOIL)"

    # Sending the message to the user's DM
    try:
        await interaction.user.send(message)
        await interaction.channel.send(f"{interaction.user.mention} has successfully generated the Logitech Recoil Script. Please check your DMs for the download link.")
    except discord.errors.Forbidden:
        await interaction.channel.send(f"{interaction.user.mention}, I couldn't send you a DM. Please make sure your DMs are open to receive the script.")

# Event to sync commands when the bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync the slash commands with Discord
    print(f"Logged in as {bot.user} and synced commands.")

# Run the bot
bot.run('MTM1NDIyNjcxOTQ0NzU4NDk1MQ.GOWVQ3.OKbgGh4L7SicsMIi-DSPEpPz0eGo9kjBLamguU')
