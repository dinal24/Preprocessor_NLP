__author__ = 'Januka'

import enchant
import operator

from collections import Counter
from math import sqrt

from Normalize import toLowerCase
from Normalize import removePunctuations
from Normalize import removeRedundantWhiteSpaces

def spellCorrect(str_input, language='en_US'):
    str_input = removeRedundantWhiteSpaces(str_input)
    str_input = toLowerCase(str_input)
    str_input = removePunctuations(str_input).split(" ")
    out_array = []
    for word in str_input:
        d = enchant.Dict(language)
        isword = d.check(word)
        if (isword):
            out_array.append(word)
        else:
            word_list = d.suggest(word)
            out = suggestions(word_list, word)
            out_array.append(out)
    output = ' '.join(out_array)

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
        out = str.replace(user_input, dict.keys()[0]).lower()
    else:
        out = max(dict.iteritems(), key=operator.itemgetter(1))[0].lower()
    return out

def word2vec(word):
    cw = Counter(word)
    sw = set(cw)
    lw = sqrt(sum(c * c for c in cw.values()))
    return cw, sw, lw

def cosdis(v1, v2):
    common = v1[1].intersection(v2[1])
    return sum(v1[0][ch] * v2[0][ch] for ch in common) / v1[2] / v2[2]

