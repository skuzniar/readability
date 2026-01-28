import os
import sys
import math

import utils.tokenizer as tokenizer
import utils.counter   as counter

def level(text, details, verbose):
    nsentences = 0
    npolysyllabicwords = 0

    paragraphs = tokenizer.paragraphs(text)

    for paragraph in paragraphs:
        sentences = tokenizer.sentences(paragraph)
        nsentences += len(sentences)

        for sentence in sentences:
            if verbose:
                print("Sentence=[", sentence, "]")
            words  = tokenizer.words(sentence)

            for word in words:
                syllables = counter.syllables(word)
                if verbose:
                    print("Word=[", word, "] syllables=", syllables)
                # TODO discout ed, es suffixes
                if syllables >= 3:
                    npolysyllabicwords += 1

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of polysyllabic words=", npolysyllabicwords)

    result = 1.043 * math.sqrt(npolysyllabicwords * 30.0 / nsentences) + 3.1291
    return result

