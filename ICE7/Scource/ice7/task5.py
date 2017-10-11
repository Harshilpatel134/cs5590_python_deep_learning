from nltk.util import trigrams
from nltk.tokenize import word_tokenize,sent_tokenize
file1=open('input.txt','r')
line =file1.readline()
print('Trigrams:')
while line !="":
       token= word_tokenize(line)
       for x in trigrams(token):
           print(x)
       line=file1.readline()