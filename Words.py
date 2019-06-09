import csv
from random import randint
import codecs

def word_generator():
    words = list(csv.reader(codecs.open('slowa.txt','r','UTF-8')))
    word = words[randint(1,len(words)-1)]
    return word[0]

#print(word_generator())