import time
import login
import settings
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix=settings.prefix)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.send('Pong! {0} ms'.format(round(bot.latency*1000,1)))
    
@bot.command()
async def test(ctx, *, arg):
    if (ctx.channel.id == settings.suggestions):
        await ctx.send(arg)

@bot.command()
async def bug(ctx, *, arg):
    buglog = bot.get_channel(settings.buglog)
    if (ctx.channel.id == settings.bugreport):
        await  buglog.send("Bug: {0} | Door {1}".format(arg,ctx.author))   
        await ctx.message.delete()
    else:
        await ctx.message.delete()        
        msg = await ctx.send("Wilt u dit even in {0} doen, danku!".format(settings.bugkanaal))
        await asyncio.sleep(1)
        await msg.delete()

@bot.command()
async def suggestie(ctx, *, arg):
    if (ctx.channel.id == settings.suggesties):
        msg = await  bot.get_channel(settings.suggesties).send("Suggestie: {0} | Door {1}".format(arg,ctx.author))   
        await ctx.message.delete()
        await msg.add_reaction('\U0001F44D')
        await msg.add_reaction('\U0001F44E')
    else:
        await ctx.message.delete()        
        msg = await ctx.send("Wilt u dit even in {0} doen, danku!".format(settings.suggesties))
        await asyncio.sleep(1)
        await msg.delete()

@bot.command()
async def reportcid(ctx):
    await ctx.send(ctx.channel.id)

bot.run(login.token)