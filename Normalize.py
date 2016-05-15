# -*- coding: utf-8 -*-
__author__ = 'dinal'

def removeRedundantWhiteSpaces(str_input):
    ret = " ".join(str_input.split())
    return ret

def toLowerCase(str_input):
    return str_input.decode('utf-8').lower()



