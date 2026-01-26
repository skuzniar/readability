import os
import sys

import utils.tokenizer as tokenizer
import utils.counter   as counter

def score(text, details, verbose):
    nparagraphs = 0
    nsentences = 0
    nwords = 0
    nsimplewords = 0
    nignoredwords = 0
    nsyllables = 0
    ncharacters = 0

    # Compount sentences (with a semicolon) are trated as two sentences.
    paragraphs = tokenizer.paragraphs(text.replace(';', '.'))
    nparagraphs = len(paragraphs)

    ignored = ["the", "is", "was", "are", "where"]

    for paragraph in paragraphs:
        sentences = tokenizer.sentences(paragraph)
        nsentences += len(sentences)

        for sentence in sentences:
            if verbose:
                print("Sentence=[", sentence, "]")
            tokens = tokenizer.tokens(sentence)
            words  = tokenizer.words(sentence)
            nwords += len(words)

            for token in tokens:
                if verbose:
                    print("Token=[", token, "]")
                ncharacters += len(token)

            for word in words:
                syllables = counter.syllables(word)
                if verbose:
                    print("Word=[", word, "] syllables=", syllables)
                nsyllables += syllables

                if syllables == 1:
                    nsimplewords += 1
                if word in ignored:
                    nignoredwords += 1

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of simple words=", nsimplewords)
        print("Number of ignored words=", nignoredwords)

    result = (100.0 * (nsimplewords - nignoredwords) + 300.0 * nsentences) / nwords
    return result

