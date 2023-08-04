import time
from gensim import models
import gensim.downloader
from keybert import KeyBERT
import re

# KeyBERT model to extract important words/phrases and block stop words from query sentence
kw_model = KeyBERT()

# Word2vec variant model to generate like terms
w2v = gensim.downloader.load('glove-twitter-25')
# time.sleep(10)


def extract_phrases(query):
    extraction = kw_model.extract_keywords(
        query, keyphrase_ngram_range=(1, 2), stop_words='english')
    keywords = [entry[0].replace(
        " ", "-") if " " in entry[0] else entry[0] for entry in extraction]
    return keywords


def retrieve_related_terms(text):
    # Check if token(term) is in the vocab
    # If so generate related terms
    # Otherwise return null to prevent errors/crashing
    if text in w2v:
        # Generate related terms
        pre_formatted_tokens = w2v.most_similar(text, topn=5)

        # Format related terms as an array terms.
        related_terms = []
        for token in pre_formatted_tokens:
            # Compare trimmed text input and related terms to ensure you don't return
            # similar values (ie. return cola for coca-cola)
            key_check = re.sub(r'[!@#$(),\n"%^*?\:;~`-]', "", token[0])
            trimmed_text = re.sub(r'[!@#$(),\n"%^*?\:;~`-]', "", text)

            # Return generated keys with spaces
            new_key = re.sub(r'[!@#$(),\n"%^*?\:;~`-]', " ", token[0])
            # print(key_check in trimmed_text, key_check, trimmed_text)

            # Only return keys that don't match the query text
            if key_check not in trimmed_text:
                related_terms.append(new_key)
        return related_terms
    else:
        return []


def generate_like_terms(query):
    keywords = extract_phrases(query)
    final_terms = []
    for word in keywords:
        related_terms = retrieve_related_terms(word)
        final_terms.extend(related_terms)
    return list(set(final_terms))
