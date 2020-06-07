#create two tuples
tup1=(1,4,5,6,7)
tup2=(5,6,7,8,9)
#concatenate both tuples
tup3=tup1+tup2
print(tup3)
#remove duplicates
tup4=tuple(set(tup3))
print(tup4)
#find index value of 9
print(tup4.index(9))
#find common elements
x=set(tup4)
y={0,4,5}
z=x.intersection(y)
print(tuple(z))
#multiple above tuple 3 times
print(tuple(z)*3)
