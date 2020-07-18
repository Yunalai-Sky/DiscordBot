import objects.champions
import requests

from bs4 import BeautifulSoup

def getlanguage(args):
    for x in args:
        if x.lower() == 'fr' or x.lower() == '_fr':
            return True
        elif x.lower() == 'en' or x.lower() == '_en':
            return False
    return 'nonegiven'


def gethelp(prefix):
    toreturn = '```\n'
    toreturn += f"Use the command as this: '{prefix}lolbuild (language - optional) (champion)' - DEFAULT is english\n"
    toreturn += f"e.g: {prefix}lolbuild fr akali or {prefix}lolbuild akali\n"
    toreturn += '```'
    return toreturn


def extractchamp(args, french):
    if french == 'nonegiven':
        return args[0]
    return args[1]


def buildchamplist(jsonlist, jsonsep):
    toreturn = []
    for x in jsonlist:
        currchamp = objects.champions.Champion(x['name'], x['nickname'].split[jsonsep])
        toreturn.append(currchamp)
    return toreturn


def getUrl(baseurl, champion):
    return baseurl + f"lol/champions/{champion}/build"


def verifychampname(userinput, listofchamp):
    for x in listofchamp:
        if userinput == x.name:
            return x.name
        else:
            for z in x.nickname:
                if userinput == z:
                    return x.name
    return userinput


def retrievehtml(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    maintree = soup.find('div', class_='perk-style-title').string
    mainrune = getkeystone(soup, 'primary-perk keystones path-keystones')
    secondmainrune = getkeystone(soup, 'primary-perk perks path-perk-1')
    thirdmainrune = getkeystone(soup, 'primary-perk perks path-perk-2')
    finalmainrune = getkeystone(soup, 'primary-perk perks path-perk-3')

    secondarytree = soup.find_all('div', class_='perk-style-title')[-1].string

    firstsecondaryrune = ""
    secondsecondaryrune = ""

    listofperk = ['perks path-perk-1', 'perks path-perk-2', 'perks path-perk-3']

    for x in listofperk:
        if firstsecondaryrune == "":
            currattempt = getkeystone(soup, x)
            if currattempt != 0:
                firstsecondaryrune = currattempt
            else:
                continue
        elif secondsecondaryrune == "":
            currsec = getkeystone(soup, x)
            if currsec != 0:
                secondsecondaryrune = currsec
                break
            else:
                continue
        else:
            break

    return [[maintree, mainrune, secondmainrune, thirdmainrune, finalmainrune], [secondarytree, firstsecondaryrune,
            secondsecondaryrune]]


def getkeystone(soup, perkname):
    activekeystone = soup.find('div', class_=f'{perkname}')
    if activekeystone is None:
        return 0
    for div in activekeystone.find_all('div', class_='perk perk-active'):
        for img in div.find_all('img', alt=True):
           return img['alt']

