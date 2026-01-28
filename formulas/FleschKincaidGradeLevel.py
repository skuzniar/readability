import os
import sys

import utils.tokenizer as tokenizer
import utils.counter   as counter

def level(text, details, verbose):
    nsentences = 0
    nwords = 0
    nsyllables = 0

    paragraphs = tokenizer.paragraphs(text)

    for paragraph in paragraphs:
        sentences = tokenizer.sentences(paragraph)
        nsentences += len(sentences)

        for sentence in sentences:
            if verbose:
                print("Sentence=[", sentence, "]")
            words  = tokenizer.words(sentence)
            nwords += len(words)

            for word in words:
                syllables = counter.syllables(word)
                if verbose:
                    print("Word=[", word, "] syllables=", syllables)
                nsyllables += syllables

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of syllables=", nsyllables)

    result = 0.39 * nwords / nsentences + 11.8 * nsyllables / nwords - 15.59
    return result

