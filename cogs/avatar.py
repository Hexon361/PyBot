import discord
import datetime
from discord.ext import commands

class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self, ctx, member : discord.Member = None):
        if member == None:
            member = ctx.author

        memberAvatar = member.avatar_url

        avaembed = discord.Embed(
            colour = discord.Colour.purple()
        )

        avaembed.timestamp = datetime.datetime.utcnow()
        avaembed.set_image(url = memberAvatar)
        avaembed.set_author(name=f'{ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')

        await ctx.send(embed = avaembed)

def setup(client):
    client.add_cog(Avatar(client))