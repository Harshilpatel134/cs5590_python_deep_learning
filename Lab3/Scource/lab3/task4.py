

from nltk.stem import WordNetLemmatizer
from collections import Counter

from nltk.tokenize import word_tokenize,sent_tokenize

from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize


f1=open('input.txt','r')
l =f1.readline()
lm=WordNetLemmatizer()

ans=[]
temp=[]
while (True):
    words = word_tokenize(l)
    for x in words:
        if(x=='.'):
            continue

        pos = pos_tag([lm.lemmatize(x)])
        if(pos[0][1]!='VB'):
            ans += [lm.lemmatize(x)]
        else:
            temp+=[lm.lemmatize(x)]
    l=f1.readline()
    if (l == ""):
        break
print("-----------lemmatization & POS tag---------")
print (ans)
print("----verb removed----")
print (temp)
newl = []
frequency = []
fr = Counter(ans).most_common(5)
print("-------top five repating words----------")
print(fr)
f1=open('input.txt','r')
l =f1.readline()
a=sent_tokenize(l)

finalans=[]
for x in fr:
    tt=str(x)[2:].split("'")

    for i in a:
        if(tt[0] in i):
            finalans+=[i]
anss=""
for i in set(finalans):
    anss+=i
print("---------final ans----------")
print(anss)