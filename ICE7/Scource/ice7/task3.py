from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
file1=open('input.txt','r')
line =file1.readline()
print('POS tagging : ')
ans=""
while line !="":
    ans=line
    line = file1.readline()

words=word_tokenize(ans)
x=pos_tag(words)
print(x)
