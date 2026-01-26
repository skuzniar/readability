import os
import sys


from nltk.corpus import cmudict

dictionary = cmudict.dict()

#referred from stackoverflow.com/questions/14541303/count-the-number-of-syllables-in-a-word
def _syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower()
    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return count 


def syllables(word):
    try:
        pronunciations = dictionary[word.lower()]
        return [len([phoneme for phoneme in pron if phoneme[-1].isdigit()]) for pron in pronunciations][0]
    except KeyError:
        return _syllables(word)

