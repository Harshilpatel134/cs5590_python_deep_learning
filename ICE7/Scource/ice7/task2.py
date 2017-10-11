from nltk.stem import SnowballStemmer
file1=open('input.txt','r')
line =file1.readline()
Stemmer =SnowballStemmer('english')
while line!="":
    words =line.split(" ")
    for word in words:
         print('Stemming of word '+word+' is : '+Stemmer.stem(word))
    line=file1.readline()