# -*- coding: utf-8 -*-
# To do all sort of NLP stuff I usually use these two, e.g. get features for models,
# Do keyword search etc., remove stopwords, etc.

from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from pattern.text.es import parse
import unicodedata

def checkText(text):
    if type(text) == str or type(text) == unicode:
        return text
    else: raise TypeError('Input should be string or unicode')

def removeStopWords(text):
    checkText(text)
    content_words = [token for token in text.split(' ') if token.lower() not in stopwords.words('spanish')]
    return content_words

def lemmatize(text):
    checkText(text)
    lemmas = [token.split('/')[-1] for token in parse(text, lemmata=True).split(' ')]
    return lemmas

def posTags(text):
    checkText(text)
    pos = [token.split('/')[1] for token in parse(text).split(' ')]
    return pos

def stemming(text):
    checkText(text)
    stems = SnowballStemmer("spanish").stem(text)
    return stems

def removeNonAscii(text):
    checkText(text)
    text = ''.join(c for c in unicodedata.normalize('NFKD', text).encode('ascii', 'ignore'))
    return text

# Examples
# print removeStopWords(u'el perro es el animal favorito de los niños', 'spanish')
# print lemmatize(u'el perro es el animal favorito de los niños')
# print posTags(u'el perro es el animal favorito de los niños')
# print stemming(u'el perro es el animal favorito de los niños')
# print removeNonAscii(u'el perro es el animal favorito de los niños')
