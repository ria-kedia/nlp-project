import difflib
f1=open("myans","r")
f2=open("correctans","r")
str1=f1.read(500)
str2=f2.read(500)
seq=difflib.SequenceMatcher(None,str2,str1)
d=seq.ratio()*100
print(d)

