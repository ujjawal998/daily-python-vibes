s={2,10,3,4,5,20}
print(s)
s.add(15)
s.add(52)
print(s)
s.remove(10)
s.remove(4)
print(s)
#s.remove(100) it will gives error because 100 is not present in set 's'
print(s)
s.discard(100)# it cannot gives error because this method is used when we are not 
#sure that element is present in set
print(s)
s.pop() #it remove random element from set 
print(s)