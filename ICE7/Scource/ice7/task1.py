
from nltk.tokenize import word_tokenize,sent_tokenize
file1=open('input.txt','r')
line =file1.readline()
while line!="":
    for sentence in sent_tokenize(line):
        print('######## word tokenization ###########')
        for words in word_tokenize(sentence):
            print(words,end=",")
        print()
    line=file1.readline()