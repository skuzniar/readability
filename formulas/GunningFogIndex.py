import os
import sys

import utils.tokenizer as tokenizer
import utils.counter   as counter

def level(text, details, verbose):
    nsentences = 0
    nwords = 0
    ncomplexwords = 0

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
                # TODO discout ed, es suffixes
                if syllables >= 3:
                    ncomplexwords += 1

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of complex words=", ncomplexwords)

    result = 0.4 * (nwords / nsentences + 100.0 * ncomplexwords / nwords)
    return result

