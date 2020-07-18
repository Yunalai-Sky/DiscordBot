from googletrans import Translator


def translateToFr(textlst):
    maintree = []
    secondarytree = []

    translator = Translator()

    for x in range(len(textlst[0])):
        maintree.append(translator.translate(textlst[0][x], src='en', dest='fr').text)

    for y in range(len(textlst[1])):
        secondarytree.append(translator.translate(textlst[1][y], src='en', dest='fr').text)

    return [maintree, secondarytree]
