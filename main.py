#This will be the main file for the bot.

#To Do:

#X- slash commands
#X- bot DMs user
#- bot creates channel
#- bot reads local XML files
#- bot outputs map image for user



#data structure for map nodes:
class mapnode:
    def __init__(self, linkedNodes=None, properties=None):
        self.linkedNodes = linkedNodes #a list of pointers [node, node, node] to adjacent nodes
        self.properties = properties #a python dictionary of other properties. Things like "can spawn here", "owner", and "local deck"
#...

#code for searching the map for things, like an unowned node for a player to spawn on or something. We can fill in the criteria later
def searchMap(node, parents = []):
    parents.append(node)
    result = None
    ## put the search criteria here...
    # if child meets some criteria: 
    #   result = child
    for child in node.linkedNodes:
        if child not in parents:
            result, parents = spanMap(child, parents)
    return result, parents
#...

######################################################################################

#Here is the (non-slash) way to DM a user

#overriding the on_message function to watch for messages in DMs
@bot.event
async def on_message(message: discord.Message):
  if message.guild is None and not message.author.bot: #if this message is a DM
    #do other stuff here
    await message.author.send("I got your dm! ```{}```".format(message.content))#Respond with a DM
  await bot.process_commands(message)#make sure to include this line, so that it processes other stuff normally
  
#how to respond to a message in the regular channel by DMing the user
@commands.guild_only()
@bot.command()
async def dm(ctx, *, args=""):
  #await bot.send_message(ctx.author, "here's a dm!")
  await ctx.author.send("here's a DM!") #send a DM to the user
  await ctx.send("I sent you a dm or two!") #send a DM in the regular channel


######################################################################################

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

######################################################################################

#Here's the minimal bot updated to include a single argument.
import interactions

bot = interactions.Client(token="token here")

@bot.command(name="test",
             description="Helptext for the command",
             options= [
                 interactions.Option(
                     name="argument1",
                     description="Helptext describing the argument",
                     type=interactions.OptionType.STRING,
                     required=False
                     )
                 ]
             )
async def test(ctx, argument1 = ""):
    #print(ctx)
    await ctx.send("args: {}".format(argument1))

bot.start()
