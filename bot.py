import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready.")

client.run('NjY0NzA3NjkxOTc2ODUxNDU2.XhbE1A.QmEJ8mhKsJdm3TQgU0uNE9AVsvc')