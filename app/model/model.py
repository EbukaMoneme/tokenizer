import time
from gensim import models
import gensim.downloader
import re

w2v = gensim.downloader.load('glove-twitter-25')
time.sleep(10)


def createTokens(text):
    pre_formatted_tokens = w2v.most_similar(text)
    formatted_tokens = {}
    for token in pre_formatted_tokens:
        key = re.sub(r'[!@#$(),\n"%^*?\:;~`]', " ", token[0])
        formatted_tokens[key] = token[1]
    return formatted_tokens
