from nltk.corpus import wordnet
from itertools import chain
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