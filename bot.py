import time
import login
import settings
from discord.ext import commands
bot = commands.Bot(command_prefix=settings.prefix)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send('Pong! {0} ms'.format(round(bot.latency*1000,1)))
    
bot.run(login.token)