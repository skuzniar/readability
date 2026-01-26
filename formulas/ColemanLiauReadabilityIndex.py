import os
import sys

import utils.tokenizer as tokenizer
import utils.counter   as counter

def level(text, details, verbose):
    nparagraphs = 0
    nsentences = 0
    nwords = 0
    ncomplexwords = 0
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
                # Exclide non-alpha-numeric
                #ncharacters += len(token)
                ncharacters += sum(char.isalnum() for char in token)

            for word in words:
                syllables = counter.syllables(word)
                if verbose:
                    print("Word=[", word, "] syllables=", syllables)
                nsyllables += syllables

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of characters=", ncharacters)

    L = 100.0 * ncharacters / nwords
    S = 100.0 * nsentences / nwords

    result = 0.0588 * L - 0.296 * S - 15.8
    return result

