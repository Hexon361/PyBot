import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

#Command = ban

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="Brak powodu"):
            await ctx.message.delete()

            embed = discord.Embed(
                title = f'{member.name} Został zbanowany',
                description = f'Powód: {reason}',
                colour = discord.Colour.red()
            )

            embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()

            await member.ban(reason=reason)
            await ctx.channel.send(embed = embed)

#Command = unban

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        await ctx.message.delete()

        for ban_entry in banned_users:
            user = ban_entry.user

            embed = discord.Embed(
                title = f'{user.name} Został odbanowany\n',
                colour = discord.Colour.green()
            )
            embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(embed = embed)

#Command = kick

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="Brak powodu"):
            await ctx.message.delete()

            embed = discord.Embed(
                title = f'{member.name} Został wyrzucony',
                description = f'Powód: {reason}',
                colour = discord.Colour.blue()
            )

            embed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()

            await member.kick(reason=reason)
            await ctx.channel.send(embed = embed)

#Command = clear

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=100):
            await ctx.channel.purge(limit=amount)
            await ctx.channel.send(f":heavy_check_mark: Pomyślnie usunięto `{amount}` wiadomości")

#Command = nuke

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def nuke(self, ctx, channel: discord.TextChannel = None):
        if channel == None: 
            await ctx.send("Musisz oznaczyć kanał 🦍")
            return

        nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

        if nuke_channel is not None:
            new_channel = await nuke_channel.clone(reason="clear")
            await nuke_channel.delete()
            await new_channel.send(f"Kanał #{channel.name} został wyczyszczony 💣")

        else:
            await ctx.send(f"Nie znaleziono {channel.name}")

#Command = error

    @ban.error
    async def ban_error(self, ctx, error, name="{}"):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'{ctx.message.author.mention} Nie posiadasz permisji 🦍'.format(ctx.message.author))

    @unban.error
    async def unban_error(self, ctx, error, name="{}"):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'{ctx.message.author.mention} Nie posiadasz permisji 🦍'.format(ctx.message.author))

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'{ctx.message.author.mention} Nie posiadasz permisji 🦍'.format(ctx.message.author))

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'{ctx.message.author.mention} Nie posiadasz permisji 🦍'.format(ctx.message.author))

    @nuke.error
    async def nuke_error(self, ctx, error, name="{}"):
        if isinstance(error, MissingPermissions):
            await ctx.send(f'{ctx.message.author.mention} Nie posiadasz permisji 🦍'.format(ctx.message.author))

def setup(client):
    client.add_cog(Mod(client))