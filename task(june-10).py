#print multiples of 8 from to and add it to list
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=[]
for i in range(a,b):
    if i%8==0:
        c.append(i)
print(c)

#print multiples of 8 and 9 and add it into two lists
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=[]
d=[]
for i in range(a,b):
    if i%8==0:
        c.append(i)
print(c)
for i in range(a,b):
    if i%9==0:
        d.append(i)
print(d)

#print odd nd even number and add it into two lists
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=[]
d=[]
for i in range(a,b):
    if i%2==0:
        c.append(i)
print(c)
for i in range(a,b):
    if i%2!=0:
        d.append(i)
print(d)
