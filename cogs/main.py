import discord
from discord.commands import Option, slash_command
from discord.ext import commands


class main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="查看機器人功能資訊")
    async def help(self, ctx):
        with open("database/help/help.txt", "r", encoding="UTF-8") as file:
            data = file.read()
        embed = discord.Embed(description=data,color=discord.Colour.random())
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(main(bot))
