from nextcord.ext import commands


class Ping(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency
        latency_ms = round(latency * 1000)

        await ctx.send(f"Pong! Latency: {latency_ms}ms")


def setup(bot):
    bot.add_cog(Ping(bot))
    