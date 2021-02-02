import discord
from discord.ext import commands
from asyncio import *
from random import randint

class CONFING:
    TOKEN = 'TOKEN OF YOUR BOT'
    PREFIX = '-'

client = commands.Bot(command_prefix = CONFING.PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot Online....")


@client.command()
async def salam(ctx):
    mention = ctx.author.mention
    await ctx.send("salam %s" % (mention))


@client.command()
async def taas(ctx):
    #a simple game
    x = randint(1, 6)
    await ctx.send("Your number is: %i" % (x))


@client.command()
async def cmd(ctx, * ,values):
    values = values.split()
    password = values[0]
    name = values[1]
    await ctx.send("password: "+password+"\n"+"name: "+name)


@client.command()
@commands.has_permissions(manage_messages = True)
async def setstatus(ctx, status_type):
    #Admin command
    if(status_type == 'idle'):
        #idle status
        await client.change_presence(status = discord.Status.idle)
        await ctx.send("status change to --> idle")
    elif(status_type == 'dnd'):
        #do not disturb message
        await client.change_presence(status = discord.Status.dnd)
        await ctx.send("status change to --> dnd")
    else:
        #online status
        await client.change_presence(status = discord.Status.online)
        await ctx.send("status change to --> online")


@client.command()
@commands.has_permissions(manage_messages = True)
async def setactivity(ctx, activity_type, * ,activity_text):
    #Admin command
    mention = ctx.author.mention
    if(activity_type == 'playing'):
        await client.change_presence(activity = discord.Game(name = activity_text))
        await ctx.send("%s. Activity changed" % (mention))


    elif(activity_type == 'streaming'):
        await client.change_presence(activity = discord.Streaming(name = activity_text,
         url ='http://twitch.tv/twitch' ))
        await ctx.send("%s. Activity changed" % (mention))


    elif(activity_type == 'listening'):
        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening,
        name = activity_text)) 
        await ctx.send("%s. Activity changed" % (mention))


    elif(activity_type == 'watching'):
        await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching,
        name = activity_text))
        await ctx.send("%s. Activity changed" % (mention))


    else:
        #unknown command
        await ctx.send("%s Unknown Activity(%s)" % (mention, activity_type))


@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 100):
    #Admin command
    await ctx.channel.purge(limit = amount)
    await ctx.send("Chat Cleared")




client.run(CONFING.TOKEN)