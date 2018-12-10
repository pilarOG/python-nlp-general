# -*- coding: utf-8 -*-
import nwalign as nw
import pandas as pd

PHON = pd.read_csv('distanciaFonetica.csv', header = 0, delimiter = ",", encoding = 'utf-8')
data2 = PHON.set_index("Unnamed: 0")

# Get a phonetic distance score between two strings in Spanish

def phoneticDistanceScore(word, comparison):
    word = transcribe(word)
    candidate = transcribe(comparison)
    # alignment betweem transcriptions
    if candidate == 'None ##' or candidate == '':
        return 1000, candidate
    at1, at2 = nw.global_align(word, candidate)

    # get phonetic matrix
    distance = 0
    l = len(at1)
    for n in xrange(0, l):
        a = at1[n]
        b = at2[n]
        if a not in (' ','  ', '-') and b not in (' ','  ', '-') and a != '#': distance += data2.loc[a,b] # substitutions
        elif a in (' ','  ', '-'): distance +=  2 # insertion
        elif b in (' ','  ', '-'): distance +=  2 # deletion
    return float(distance)/float(l), comparison

def transcribe(input):
    word = input.replace(u'ú','U').replace(u'á','A').replace(u'é','E').replace(u'í','I').replace(u'ó','O').replace('qu','k').replace('q','k').replace('y','i').replace('j','x').replace('v','b').replace('z','s').replace('w','u').replace(u'ñ','N')
    word = word.replace('ce', 'se').replace('ci', 'si').replace('ch', 'C')
    word = word.replace('ge', 'x').replace('gi', 'x')
    word = word.replace('ll','L').replace('h','').replace('rr', 'R')
    word = word.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
    word = word.replace('c','k').replace(',','').replace('\'','').replace('.','').replace('?','').replace(')','').replace('(','').replace(u'´','')
    word = '#'+word+'#'
    return word

# The closer the result to 0 the more similar the two strings
print phoneticDistanceScore('cazar', 'casar') # Same pronunciation, different orthography
print phoneticDistanceScore('cazar', 'pasar') # Similar orthography, different pronunciation
