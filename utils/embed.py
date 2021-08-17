    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.timestamp = datetime.datetime.utcnow()
    embed.set_image(url = memberAvatar)
    embed.set_footer(text='\u200b')
    embed.set_author(name=f'{ctx.message.author}', icon_url='https://cdn.discordapp.com/avatars/384345701305548812/a_d71c1f6a22b41d3425ee4408a68f65d5.gif?size=1024')


    await ctx.send(embed = embed)