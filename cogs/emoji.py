from PIL import Image
import requests
import discord
from discord.ext import commands
from io import BytesIO
import os

class Emoji(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def emoji(self, ctx, object, *, name):
        guild = ctx.guild
        if ctx.author.guild_permissions.manage_emojis:
            r = requests.get(object)
            img = Image.open(BytesIO(r.content), mode='r')
            try:
                img.seek(1)
            except EOFError:
                is_animated = False

            else:
                is_animated = True

            if is_animated == True:
                await ctx.send('Jebac animowane')

            elif is_animated == False:
                b = BytesIO()
                img.save(b, format='PNG')
                b_value = b.getvalue()
                emoji = await guild.create_custom_emoji(image=b_value, name=name)
                await ctx.send(f'Dodano emotke: {name} {emoji.id}')

def setup(client):
    client.add_cog(Emoji(client))