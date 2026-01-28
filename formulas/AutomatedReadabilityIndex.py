import os
import sys

import utils.tokenizer as tokenizer

def level(text, details, verbose):
    nsentences = 0
    nwords = 0
    ncharacters = 0

    paragraphs = tokenizer.paragraphs(text)

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

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of characters=", ncharacters)

    result = 4.71 * ncharacters / nwords + 0.5 * nwords / nsentences - 21.43
    return result
