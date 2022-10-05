from tokenize import Token
from turtle import reset
from unittest import result
import discord
from discord.ext import commands
import json
with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents = intents)

#bot上線    
@bot.event
async def on_ready():
    print(">> Bot is online <<")
#成員進伺服器
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['小廳'])) #傳訊息的頻道ID
    await channel.send(f'{member}join')
#成員離開伺服器
@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(int(jdata['小廳'])) 
    await channel.send(f'{member}leave')
#回傳機器人延遲ping值
@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)') #小數點四捨五入進位 單位毫秒


bot.run(jdata['TOKEN'])