import discord
import asyncio
from secretcode import *
from discord.ext import commands
from discord.utils import get

# activity=discord.Game(name='Currently being better than Shy')
# activity=discord.Streaming(name='SHY IS STREAMING',
# url='https://twitch.tv/gracefullyshy')
bot = commands.Bot(command_prefix='_', activity=discord.Activity(
    type=discord.ActivityType.watching, name='just alive for a bit'),
                   status=discord.Status.do_not_disturb)


# @commands.command()
# async def test(ctx, arg):
#     await ctx.send(arg)

# bot.add_command(test)

# @bot.command(name='list')
# async def _list(cxt, arg):
#     pass

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(f'Pong! Our connection took {latency} seconds to process')


@bot.command()
async def pong(ctx):
    await ctx.send('ping')


@bot.command()
async def boop(ctx):
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send('*booooooop*')


@bot.command()
@commands.has_role('Schnurble')
async def say(ctx, arg):
    await ctx.message.delete()
    await ctx.send(arg)


@bot.command()
@commands.has_role('Schnurble')
async def intro(ctx):
    person = '<@268883249151868928>'
    await ctx.message.delete()
    await ctx.send("""Name/What to call me - Schnurble
Pronouns - He/They
Age - yes
One of my indigos - Being a part of this community
Favorite Minecraft mob/animal - Fox
Likes - Nice people, games, watching stream, and music
Dislikes - When people don't notice that I'm offline and try to use my commands
Random fun fact - I was created by %s""" % person)


@bot.command()
@commands.has_role('Staff')
async def mute(ctx, arg):
    await ctx.send('Nah, I don\'t really feel like muting ' + arg)


@bot.command()
@commands.has_role('Schnurble')
async def purge(ctx, number):
    number = int(number)
    await ctx.channel.purge(limit=number)


@bot.command()
@commands.has_role("Schnurble")
async def ban(ctx):
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send(
        'I\'ve said it once and I\'ll say it again, we should ban Juru')


bot.run(secret_code)
