import os
import sys

import utils.tokenizer as tokenizer
import utils.counter   as counter

def score(text, details, verbose):
    nparagraphs = 0
    nsentences = 0
    nwords = 0
    nsyllables = 0
    ncharacters = 0

    paragraphs = tokenizer.paragraphs(text)
    nparagraphs = len(paragraphs)

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
                if verbose:
                    print("Word=[", word, "] syllables=", counter.syllables(word))
                nsyllables += counter.syllables(word)

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of syllables=", nsyllables)

    result = 206.835 - 1.015 * nwords / nsentences - 84.6 * nsyllables / nwords
    return result

