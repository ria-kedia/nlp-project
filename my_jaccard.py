import nltk
from nltk.tokenize import word_tokenize

from nltk.stem.wordnet import WordNetLemmatizer
f1=open("myans.txt","r")
f2=open("correctans.txt","r")
str1=f1.read(300)
str2=f2.read(300)

lemma_a=[]
tokens_a=nltk.tokenize.word_tokenize(str1)
for t in tokens_a:
    lemma_a.append(WordNetLemmatizer().lemmatize(t,"v"))
print(lemma_a)
lemma_b=[]
tokens_b=nltk.tokenize.word_tokenize(str2)
for p in tokens_b:
    lemma_b.append(WordNetLemmatizer().lemmatize(p,"v"))
print(lemma_b)
ratio = len(set(lemma_a).intersection(lemma_b)) / float(len(set(lemma_a).union(lemma_b)))
print(ratio)

