from nltk import bigrams, trigrams
from collections import defaultdict
import random
import pickle
import codecs
import sys

def trainNgrams(text):
    # set default dicts
    triModel, biModel, uniModel = defaultdict(lambda: 0), defaultdict(lambda: 0), defaultdict(lambda: 0)

    # it will take as sentences those separated by a dot or a new line
    for sentence in corpora.replace('.', '\n').split('\n'):
        model = 'character level'
        # ir supports both word level or character level n-grams
        if len(sys.argv) > 2:
            if sys.argv[2] == 'word':
                sentence = sentence.lower().split(' ') # word level LM #TODO: improve tokenization
                model = 'word level'
            elif sys.argv[2] == 'character': pass
            else: raise Exception('Second argument in terminal should be \'word\' or \'character\'')

        # take counts and store in dictionaries, save as string keys
        for i in sentence:
            uniModel[i] += 1
        for t1, t2, t3 in trigrams(sentence, pad_right=True, pad_left=True):
            triModel[unicode(t1)+' '+unicode(t2)+' '+unicode(t3)] += 1
        for b1, b2 in bigrams(sentence, pad_right=True, pad_left=True):
            biModel[unicode(b1)+' '+unicode(b2)] += 1

    # save count dictionaries as pickles
    with open('trigram_count', 'wb') as handle: pickle.dump(dict(triModel), handle)
    with open('bigram_count', 'wb') as handle: pickle.dump(dict(biModel), handle)
    with open('unigram_count', 'wb') as handle: pickle.dump(dict(uniModel), handle)

    # print some stats
    print 'You trained a {} N-gram model'.format(model)
    print 'Unigrams: {}; Bigrams: {}; Trigrams: {}'.format(len(uniModel), len(biModel), len(triModel))
    print 'Unigram sample: {}'.format(random.choice(uniModel.items()))
    print 'Bigram sample: {}'.format(random.choice(biModel.items()))
    print 'Trigram sample: {}'.format(random.choice(triModel.items()))

if __name__=='__main__':
    # open data, a simple txt file with text
    if len(sys.argv) == 1: raise Exception('Run this script in your terminal with the name of your file-data as first argument')
    corpora = codecs.open(sys.argv[1], 'rb', encoding='utf-8').read()
    # TODO: do normalization
    trainNgrams(corpora)
