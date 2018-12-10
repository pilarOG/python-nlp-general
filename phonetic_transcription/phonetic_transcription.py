# -*- coding: utf-8 -*-

# very simple function to transcribe pseudo phonetically words in Spanish

def transcribe(input):
    word = input.replace(u'ú','U').replace(u'á','A').replace(u'é','E').replace(u'í','I').replace(u'ó','O').replace('qu','k').replace('q','k').replace('y','i').replace('j','x').replace('v','b').replace('z','s').replace('w','u').replace(u'ñ','N')
    word = word.replace('ce', 'se').replace('ci', 'si').replace('ch', 'C')
    word = word.replace('ge', 'x').replace('gi', 'x')
    word = word.replace('ll','L').replace('h','').replace('rr', 'R')
    word = word.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
    word = word.replace('c','k').replace(',','').replace('\'','').replace('.','').replace('?','').replace(')','').replace('(','').replace(u'´','')
    word = '#'+word+'#'
    return word


print transcribe('hola')
print transcribe('perro')
print transcribe('caza')
