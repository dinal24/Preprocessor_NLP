# -*- coding: utf-8 -*-
__author__ = 'dinal'

def removeRedundantWhiteSpaces(str_input):
    ret = " ".join(str_input.split())
    return ret

def toLowerCase(str_input):
    return str_input.decode('utf-8').lower()

def removePunctuations(str_input):
    ret = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in str_input:
        if char not in punctuations:
            ret.append(char)

    return "".join(ret)

