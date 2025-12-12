s1={1,2,3}
s2={3,4,5}
print(s1.union(s2))#it will print all unique values from  both sets 
d=s1.intersection(s2)#it will print common values from both sets 
print(d)
e=s1.difference(s2)#it will print values which are only in set s1 
print(e)
f=s2.difference(s1)#it will print values which are only in set s2
print(f)
g=s2.symmetric_difference(s2) # it will print values which are not common in both sets 
print(g)
h=s2.issubset(s1) 
print(h)
i=s1.issuperset(s2)
print(i)
