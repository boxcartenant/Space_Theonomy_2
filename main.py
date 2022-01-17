#This will be the main file for the bot.
#Here is the minimal bot from the discord-interactions library for slash commands:

import interactions

bot = interactions.Client(token="...")

@bot.command(
    name="test",
    description="this is just a test command.",
    scope=1234567890
)
async def test(ctx):
    await ctx.send("Hello world!")

bot.start()
