# -*- coding: utf-8 -*-
from random import randint
import re

# This function is to modify a text with common orthographic errors from children
# usually given by spanish ortography-phonetics
# This was particularly usefull to get parallel data to train a spell checker fol children

# Subtituions dictionary
subs = {'rr':'r', # substitutions
        'nv':'nb',
        'mb':'nb',
        'd':'b', # orthography
        'v':'b',
        'b':'v',
        'y':'i',
        'z':'s',
        'ce':'se',
        'ci':'si',
        'qu':'k',
        'ca':'ka',
        'co':'ko',
        'cu':'ku',
        'ge':'je',
        ' h':' ',
        'á':'a', # diacritic omition
        'é':'e',
        'í':'i',
        'ó':'o',
        'ú':'u',
        'tr':'t', # cluster simplification
        'br':'b',
        'pl':'p',
        's ': ' ', # s aspiration
        '.': '',
        ',': ''} # punctuation

# Random factor: if = 1, most of the errors will be applied,
# the larger, the less likely the errors will apply
N = 3

# Subtitution function
def substitute(text, old, new):
    r = randint(1, N)
    if r == 1:
        text = text.replace(old, new, r)
    return text

# Lower some capitalized letters
def lowCap(text):
    for x in range(0, len(text)):
        r = randint(1, N)
        if text[x].isupper() and r == 1:
            text = text[:x]+text[x:x+1].replace(text[x], text[x].lower())+text[x+1:]
    return text

# Simplify letters that are the same at the end of a word and at the beginning of the next one
def simplify(text):
    r = randint(1, N)
    if r == 1:
        j = re.findall(r'\w\s\w', text)
        if j != []:
            for h in j:
                if h[0] == h[2]:
                    r = randint(1, N)
                    if r == 1:
                        text = text.replace(''.join(h), ' '+h[-1])
                    elif r == 2:
                        text = text.replace(''.join(h), h[0]+' ')
                    elif r == 3:
                        text = text.replace(''.join(h), h[-1])
                    elif r == 4:
                        text = text.replace(''.join(h), h[0])
    return text

# Remove space from words, combining them
def noSpace(text):
    for x in range(0, len(text)):
        r = randint(1, N)
        if text[x] == ' ':
            if randint(0, 1) == 1:
                new = text[:x]+text[x:x+1].replace(text[x], '')+text[x+1:]
    return text

# Add a white space at syllabic margins of words
def syllSplit(text):
    r = randint(1, N)
    cv = re.findall('([qwrtypsdfghjklñzxcvbnm][aeiouáéúíó])[qwrtypsdfghjklñzxcvbnm][aeiouáéúíó]', text)
    cvc = re.findall('([qwrtypsdfghjklñzxcvbnm][aeiouáéúíó][qwrtypsdfghjklñzxcvbnm])[qwrtypsdfghjklñzxcvbnm]', text)
    if cv != [] and r == 1:
        for n in cv:
            if randint(0, 1) == 1:
                r = randint(1, 4)
                text = text.replace(n, n+' ', r)
    if cvc != [] and r == 1:
        for n in cvc:
            if randint(0, 1) == 1:
                r = randint(1, 4)
                text = text.replace(n, n+' ', r)
    return text

### MAIN FUNCTION ###
def ortErrors(text):
    text = syllSplit(text)
    text = noSpace(text)
    text = simplify(text)
    text = lowCap(text)
    for k in subs:
        if k in text:
            text = substitute(text, k, subs[k])
    return text

# Example
if __name__=='__main__':
    print ortErrors('la abuela le hace cariño al perro y a la vaca')

# outcomes with N = 3
# 'la abuela le ha ce ca riño al pero y a la vaca'
# 'la avuela le ace cariño al perro i a la vaca'
# 'la abuela le ha ce cariño al pero y a la baca'
