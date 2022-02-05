import discord  #importing discord module
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = '.') #defining our bot client

#making our first event
@bot.event
async def on_ready():
  print("Bot is ready!") #Prints "Bot is ready" once our bot starts

#making our first command
@bot.command()
async def hello(ctx): # defining our command and parameters
  await ctx.reply("Hello there!") # Bot responds to our message

token = os.environ['token'] #protecting our token using os module
#if you don't want this you can just use 
#bot.run("your_token")
bot.run(token) #starting our bot