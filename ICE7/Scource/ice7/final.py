
from nltk.corpus import wordnet
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.util import trigrams
from nltk.tokenize import word_tokenize,sent_tokenize

from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize

ans=[]
f1=open('input.txt','r')
l =f1.readline()
while (True):

    words = l.split(" ")
    for word in words:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                ans+=[l.name()]
        if ans:
            print("meaning of word ",word," : ",ans)
            ans=[]
    l=f1.readline()
    if(l==""):
        break
print("\n\n\n")
print('######## word tokenization ###########')
print("\n")
f1=open('input.txt','r')
l=f1.readline()
while (True):
    for s in sent_tokenize(l):
        for words in word_tokenize(s):
            print(words,end=",")
        print()
    l=f1.readline()
    if (l == ""):
        break
print("\n\n\n")
print('######## Stemming ###########')
print("\n")
f1=open('input.txt','r')
l =f1.readline()
Stemmer =SnowballStemmer('english')
while (True):
    words =l.split(" ")
    for word in words:
         print(word + ' : '+Stemmer.stem(word))
    l=f1.readline()
    if (l == ""):
        break
print('######## POS ###########')
print("\n")
f1=open('input.txt','r')
l =f1.readline()
Stemmer =SnowballStemmer('english')
while (True):
    words =l.split(" ")
    for word in words:
         print(word + ' : '+Stemmer.stem(word))
    l=f1.readline()
    if (l == ""):
        break
print('######## Lemmatization ###########')
print("\n")
f1=open('input.txt','r')
l =f1.readline()
lemma=WordNetLemmatizer()
Stemmer =SnowballStemmer('english')
while (True):
    words = word_tokenize(l)
    for x in words:
        print(x+' : '+lemma.lemmatize(x))
    l=f1.readline()
    if (l == ""):
        break
print('######## Trigrams ###########')
print("\n")
f1=open('input.txt','r')
l =f1.readline()
lemma=WordNetLemmatizer()
Stemmer =SnowballStemmer('english')
while (True):
    token = word_tokenize(l)
    for x in trigrams(token):
        print(x)
    l=f1.readline()
    if (l == ""):
        break
print('######### named entity recoganization ########')
f=open('input.txt','r')
t =f.readline()
while (True):
    s1=ne_chunk(pos_tag(word_tokenize(t)))
    print(s1)
    t=f.readline()
    if (t == ""):
        break