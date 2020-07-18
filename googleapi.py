from googletrans import Translator


def translateToFr(textlst):
    translator = Translator()

    maintreegoogle = translator.translate(textlst[0], src='en', dest='fr')
    secondarytreegoogle = translator.translate(textlst[1], src='en', dest='fr')

    maintree = list(map(gettext, maintreegoogle))
    secondarytree = list(map(gettext, secondarytreegoogle))

    return [maintree, secondarytree]


def gettext(googleresponse):
    return googleresponse.text


def translate(message, srclang, destlang):
    translator = Translator()

    return translator.translate(message, src=srclang, dest=destlang).text
