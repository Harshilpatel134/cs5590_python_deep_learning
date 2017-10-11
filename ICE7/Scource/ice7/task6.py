from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize
f=open('input.txt','r')
t =f.readline()
print('######### named entity recoganization ########')
while (t!=""):
    s1=ne_chunk(pos_tag(word_tokenize(t)))
    print(s1)
    t=f.readline()