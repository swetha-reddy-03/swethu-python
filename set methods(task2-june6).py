#create two empty sets
s1=set()
s2=set()
print(s1)
print(s2)
#assign the elements to empty set
s1=set([7,8,9,1,2,3,4,5,0])
s2=set([4,5,6,0])
print(s1)
print(s2)
#check whether set2 is subset to set1
print(s2.issubset(s1))
#check whether both are disjoint
print(s2.isdisjoint(s1))
#remove 8 from set1
s1.remove(8)
print(s1)
#discard 0 from set2
s2.discard(0)
print(s2)
#find sum of set1 union set2
x=s1.union(s2)
print(sum(x))


