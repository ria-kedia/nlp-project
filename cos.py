import math
from collections import Counter

ListA = "Communication is basically passing of information ideas facts opinions emotions from one person to another It can also be defined as the sum of all things a person does to create understanding in the mind of another person".split()
ListB = "Communication is basically passing of information ideas facts opinions emotions from one person to another It can also be defined as the sum of all things a person does to create understanding in the mind of another person".split()
print(ListA)
print(ListB)
def cosdis(v1, v2):
        common = v1[1].intersection(v2[1])
        return sum(v1[0][ch] * v2[0][ch] for ch in common) / v1[2] / v2[2]

def word2vec(word):
    cw = Counter(word)
    sw = set(cw)
    lw = math.sqrt(sum(c * c for c in cw.values()))
    return cw, sw, lw

def removePunctuations(str_input):
    ret = []
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in str_input:
        if char not in punctuations:
            ret.append(char)
                                                                
    return "".join(ret)


for i in ListA:
    for j in ListB:
        print(cosdis(word2vec(removePunctuations(i)), word2vec(removePunctuations(j))))

