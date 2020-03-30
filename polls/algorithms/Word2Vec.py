import gzip
import gensim
import logging
import os
import codecs
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO)


def give_Word2VecSinonims(word):
    model = KeyedVectors.load("C:\Facultate\AI\Proj\ProiectAI\polls\\algorithms\model.model")
    try:
        wordToVecWords = model.wv.most_similar(positive=word)
    except:
        pass
    else:    
        words = []
        for wor in wordToVecWords:
            words.append(wor[0])
        return words
    return []