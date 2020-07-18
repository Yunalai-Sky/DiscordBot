import objects.champions

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


