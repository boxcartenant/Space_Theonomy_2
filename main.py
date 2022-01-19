#This will be the main file for the bot.

#To Do:

#- slash commands
#- bot DMs user
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

