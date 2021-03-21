import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
import youtube_dl
from urllib.request import urlopen, Request
import urllib
import urllib.request

import load_json_variable as variable

prefix = "!"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    game = discord.Game("!케인인님도와줘요|도움말열기")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")


@bot.event
async def on_message(message):
 
    if message.author.bot:
        return None

    await bot.process_commands(message)

@bot.command(name="돌려라맨이야")
async def roll(ctx, number: int):
    await ctx.channel.send(f'{random.randint(1,number)} 를! 뽑았단다맨이야! (범위: 1-{number})')

@roll.error
async def roll_error(ctx, error):
    await ctx.send("얘는 그냥! 그게 맞는 숫자니?")

@bot.command(name="아이고난!")
async def react(ctx):
    await ctx.channel.send("아이~고 난!")

@bot.command(name="뭉탱이")
async def react1(ctx):
    await ctx.channel.send("https://tenor.com/view/%ec%bc%80%ec%9d%b8-%ec%a3%84%ec%86%a1%ed%95%a9%eb%8b%88%eb%8b%a4-kane-tv-kane-%eb%ad%89%ed%83%b1%ec%9d%b4-gif-19912401")

@bot.command(name="ㅅㅅㄱㅇ")
async def react2(ctx):
    await ctx.channel.send("https://tenor.com/view/%ec%bc%80%ec%9d%b8-%ec%84%b9%ec%8b%9c%eb%8c%84%ec%8a%a4-%ec%bc%80%ec%9d%b8%ec%84%b9%ec%8b%9c%eb%8c%84%ec%8a%a4-%ec%bc%80%ec%9d%b8tv-kanetv-gif-19962072")

@bot.command(name="오늘롤")
async def lol(ctx):
    randomNum = random.randrange(1, 3)
    if randomNum==1:
        await ctx.channel.send(embed=discord.Embed(title="도망가지마! 맞서싸워!", color=discord.Color.blue()))
    else:
        await ctx.channel.send(embed=discord.Embed(title="죽어버려", color=discord.Color.red()))

@bot.command(name="케인인님도와줘요")
async def help(ctx):
    await ctx.channel.send("'텐노 헤이까, 반쟈이 !'")

bot.run(variable.get_token())