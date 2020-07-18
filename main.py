import discord
import json
import os

import lolbuildutils
import objects.champions as champion

from discord.ext import commands

champlst = []

with open('json/config.json') as data_file:
    data = json.load(data_file)
    for x in data['champList']:
        champlst.append(champion.Champion(x['name'], x['nickname'].split(data['champNicknameSep'])))


token = data['discordToken']
bot = commands.Bot(command_prefix=data['commandPrefix'])
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command(name='help')
async def help(ctx, *args):
    for x in args:
        if x.lower() == "lolbuild":
            await ctx.send(lolbuildutils.gethelp(data['commandPrefix']))
            break


@bot.command(name='lolbuild')
async def lolbuild(ctx, *args):
    if len(args) > 2:
        await ctx.send('Incorrect use of command!')
        await ctx.send(lolbuildutils.gethelp(data['commandPrefix']))
        return
    isFrench = lolbuildutils.getlanguage(args)
    champion = lolbuildutils.verifychampname(lolbuildutils.extractchamp(args, isFrench), champlst)
    await ctx.send(data['baseUrl'] + f'lol/champions/{champion}/build')

bot.run(token)
