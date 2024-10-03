import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


#habilitacion de intents
intents = discord.Intents.all()
intents.messages = True
intents.members = True

#prefijo del bot y handler
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}',description='Bot desarrollado por Noxu',color=discord.Color.blue())
    embed.add_field(name="Server owner",value=f"{ctx.guild.owner}")
    embed.add_field(name="Server created at", value=f'{ctx.guild.created_at}')
    embed.add_field(name="Server ID", value=f'{ctx.guild.id}')
    embed.add_field(name="Contenido de clase guild guild", value=f'{ctx.guild}')
    embed.set_thumbnail(url=f'{ctx.guild.icon}')
    await ctx.send(embed=embed)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'buen dia' in message.content.lower():
        await message.channel.send(f'Buen dia {message.author.name}!')

    ''' if 'yes' in message.content.lower():
        await message.channel.send(f'{message.author.name} eres un yes')
    await bot.process_commands(message) '''

    
    if 'kity mily' in message.content.lower():
        await message.channel.send(f'vas a caer kity mily')
    await bot.process_commands(message)

bot.run(TOKEN)
