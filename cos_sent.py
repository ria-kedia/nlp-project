import nltk
from nltk import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop=set(stopwords.words("english"))
f1=open("myans.txt","r")

f2=open("correctans.txt","r")

str1=f1.read(300)
str2=f2.read(300)
str1=str1.replace("."," ")
str1=str1.replace(","," ")
str2=str2.replace("."," ")
str2=str2.replace(","," ")
print("student's answer tokens are:")
tokens=nltk.word_tokenize(str1)
for i in tokens:
    if i not in stop:
        print(i)
tokens1=nltk.word_tokenize(str2)
print("correct answer's tokens are:")
for j in tokens1:
    if j not in stop:
        print(j)
        
def word2vec(word):
    from collections import Counter
    from math import sqrt

                # count the characters in word
    cw = Counter(word)
                        # precomputes a set of the different characters
    sw = set(cw)
                                # precomputes the "length" of the word vector
    lw = sqrt(sum(c*c for c in cw.values()))

                                        # return a tuple
    return cw, sw, lw

def cosdis(v1, v2):
            # which characters are common to the two words?
    common = v1[1].intersection(v2[1])
                                                        # by definition of cosine distance we have
    return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]
va=word2vec(str1)
vb=word2vec(str2)
print(cosdis(va,vb))
