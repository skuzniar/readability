import os
import sys
import math

import utils.tokenizer as tokenizer
import utils.counter   as counter

def level(text, details, verbose):
    nparagraphs = 0
    nsentences = 0
    nwords = 0
    npolysyllabicwords = 0
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
                syllables = counter.syllables(word)
                if verbose:
                    print("Word=[", word, "] syllables=", syllables)
                nsyllables += syllables
                # TODO discout ed, es suffixes
                if syllables >= 3:
                    npolysyllabicwords += 1

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of polysyllabic words=", npolysyllabicwords)

    result = 1.043 * math.sqrt(npolysyllabicwords * 30.0 / nsentences) + 3.1291
    return result

