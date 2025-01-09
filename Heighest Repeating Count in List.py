from collections import Counter
a=[10,20,30,30,10,30]
c=Counter(a)
print(max(c,key=c.get))
