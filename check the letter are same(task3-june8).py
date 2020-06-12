#check whether the first, last and middle letters are same
x=input("enter the string: ")
y=int(len(x)/2)
z=x[y]
if x[0]==z==x[-1]:
    print("True")
else:
    print("false")
