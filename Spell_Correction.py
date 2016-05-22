import enchant
from collections import Counter
from math import sqrt

def spellCorrect(user_input):
    user_input = user_input.lower()
    user_input = removePunctuations(user_input).split(" ")
    out_array = []
    for i in user_input:
        d = enchant.Dict("en_US")
        word = d.check(i)
        if (word):
            out_array.append(i)
        else:
            word = d.suggest(i)
            out = suggestions(word, i)
            out_array.append(out)
    output = ' '.join(out_array)
    print output
    return output


def suggestions(word, user_input):
    dict = {}
    for i in word:
        key_in_dict = i
        Va = word2vec(i)
        Vb = word2vec(user_input)
        cos = cosdis(Va, Vb)
        if (cos > 0.85):
            dict[key_in_dict] = cos
        else:
            pass

    if (len(dict) == 1):
        str = user_input
        out = str.replace(user_input, dict.keys()[0])
    else:
        out = user_input
    return out

def word2vec(word):

    cw = Counter(word)
    sw = set(cw)
    lw = sqrt(sum(c * c for c in cw.values()))
    return cw, sw, lw

def cosdis(v1, v2):

    common = v1[1].intersection(v2[1])
    return sum(v1[0][ch] * v2[0][ch] for ch in common) / v1[2] / v2[2]

def removePunctuations(input):
    no_punct = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in input:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct
