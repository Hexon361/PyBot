import discord
import os
import datetime
from discord.ext import commands

os.system('cls' if os.name == 'nt' else 'clear')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', case_insensitive = True , intents = intents)

client.remove_command("help")

@client.event
async def on_member_join(self, member):
    guild = client.get_guild(683343195374878834)
    channel = guild.get_channel(876803505099276318)
    await ctx.channel.send(f'Witamy na serwerze {member.mention}')

@client.group(invoke_without_command=True)
async def help(ctx):

    embed = discord.Embed(
        title = 'Help',
        description = 'Spis komend',
        colour = discord.Colour.gold()
    )

    embed.add_field(name = "Administracja", value = "Ban\nKick\nClear\nNuke\nMute\nUnmute")
    embed.add_field(name = "Użytkownicy", value = "Avatar")
    embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

@help.command()
async def ban(ctx):

    embed = discord.Embed(
        title = 'Ban',
        description = 'Banuje użytkownika z discorda',
        colour = discord.Colour.gold()
    )

    embed.add_field(name = "`Syntax`", value = "!ban <member> [reason]")
    embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

@help.command()
async def kick(ctx):

    embed = discord.Embed(
        title = 'Kick',
        description = 'Wyrzuca użytkownika z discorda',
        colour = discord.Colour.gold()
    )
    
    embed.add_field(name = "`Syntax`", value = "!kick <member> [reason]")
    embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

@help.command()
async def clear(ctx):

    embed = discord.Embed(
        title = 'Clear',
        description = 'Usuwa dana liczbe wiadomości z kanału - max 100',
        colour = discord.Colour.gold()
    )

    embed.add_field(name = "`Syntax`", value = "!clear <amount>")
    embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()


    await ctx.send(embed = embed)

@help.command()
async def nuke(ctx):

    embed = discord.Embed(
        title = 'Nuke',
        description = 'Usuwa i tworzy kanał z takimi samymi permisjami jak poprzedni',
        colour = discord.Colour.gold()
    )

    embed.add_field(name = "`Syntax`", value = "!nuke #<channel_name>")
    embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

@help.command()
async def avatar(ctx):

    embed = discord.Embed(
        title = 'Avatar',
        description = 'Pokazuje avatar danego użytkownika',
        colour = discord.Colour.gold()
    )

    embed.add_field(name = "`Syntax`", value = "!avatar <member>")
    embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

@help.command()
async def mute(ctx):

    embed = discord.Embed(
        title = 'Mute',
        description = 'Mutuje danego użytkownika',
        colour = discord.Colour.gold()
    )

    embed.add_field(name = "`Syntax`", value = "!mute <member>")
    embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

@help.command()
async def unmute(ctx):

    embed = discord.Embed(
        title = 'Unmute',
        description = 'Odmutowywuje danego użytkownika',
        colour = discord.Colour.gold()
    )

    embed.add_field(name = "`Syntax`", value = "!unmute <member>")
    embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('TOKEN')