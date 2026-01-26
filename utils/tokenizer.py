import nltk
from nltk.corpus   import cmudict
from nltk.tokenize import RegexpTokenizer

stokenizer = RegexpTokenizer(r'\w+')
dictionary = cmudict.dict()

def paragraphs(text):
    return [p for p in text.split('\n') if p]

def sentences(text):
    return nltk.sent_tokenize(text)

def tokens(text):
    return nltk.word_tokenize(text)

def words(text):
    return stokenizer.tokenize(text)

