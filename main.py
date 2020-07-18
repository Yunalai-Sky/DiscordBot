import discord
import json
import os

import lolbuildutils
import objects.champions as champion
import googleapi

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
        await ctx.send('Incorredct use of comman!')
        await ctx.send(lolbuildutils.gethelp(data['commandPrefix']))
        return
    isFrench = lolbuildutils.getlanguage(args)
    champion = lolbuildutils.verifychampname(lolbuildutils.extractchamp(args, isFrench), champlst)
    url = data['baseUrl'] + f'lol/champions/{champion}/build/'
    await ctx.send(url)
    runecontent = lolbuildutils.retrievehtml(url)

    if isFrench:
        runecontent = googleapi.translateToFr(runecontent)

    splitter = '---------------\n'

    tosend = '```\n'
    tosend += splitter

    for x in range(len(runecontent[0])):
        if x == 0:
            tosend += f'{runecontent[0][x]}\n'
            continue
        tosend += f'{runecontent[0][x]}\n'
    tosend += splitter
    for y in range(len(runecontent[1])):
        if y == 0:
            tosend += f'{runecontent[1][y]}\n'
        else:
            tosend += f'{runecontent[1][y]}\n'
    tosend += splitter
    tosend += '```'

    await ctx.send(tosend)

bot.run(token)
