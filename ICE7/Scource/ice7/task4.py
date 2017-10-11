from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
file1=open('input.txt','r')
line =file1.readline()
lemma=WordNetLemmatizer()
print('Lemmatization : ')
while line !="":
    words=word_tokenize(line)
    for x in words:
        print(x+' : '+lemma.lemmatize(x))
    line=file1.readline()