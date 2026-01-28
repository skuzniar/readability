import os
import sys

import utils.tokenizer as tokenizer
import utils.counter   as counter

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer(language="english")

from nltk.corpus import words

def is_english_word(word):
    return word.lower() in words.words()

def remove_stem(word):
    if word.endswith('ed') or word.endswith('es'):
        stem = stemmer.stem(word)
        if is_english_word(stem):
            return stem
    return word

def remove_stem_fast(word):
    if (word.endswith('ed') or word.endswith('es')):
        return stemmer.stem(word)
    return word


def level_simple(text, details, verbose):
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

                if syllables >= 3:
                    ncomplexwords += 1

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of complex words=", ncomplexwords)

    result = 0.4 * (nwords / nsentences + 100.0 * ncomplexwords / nwords)
    return result

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
                stem = remove_stem(word)
                syllables = counter.syllables(stem)
                if verbose:
                    print("Word=[", word, "] Stem=[", stem, "] syllables=", syllables)

                if syllables >= 3:
                    ncomplexwords += 1

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of complex words=", ncomplexwords)

    result = 0.4 * (nwords / nsentences + 100.0 * ncomplexwords / nwords)
    return result

def level_fast(text, details, verbose):
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
                stem = remove_stem_fast(word)
                syllables = counter.syllables(stem)
                if verbose:
                    print("Word=[", word, "] Stem=[", stem, "] syllables=", syllables)

                if syllables >= 3:
                    ncomplexwords += 1

    if details or verbose:
        print("Number of sentences=", nsentences)
        print("Number of words=", nwords)
        print("Number of complex words=", ncomplexwords)

    result = 0.4 * (nwords / nsentences + 100.0 * ncomplexwords / nwords)
    return result

