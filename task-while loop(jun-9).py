#print even numbers from 0 to 20
num = 0
while num <=20:
    if num % 2 == 0:
        print(num)
    num = num + 1
print("closed")

#print only even numbers from <user input> to <user input>

i=int(input("enter the first number"))
l=int(input("enter the second number"))
while i<=l:
    if i%2==0:
        print(i)
        i=i+2
print("closed")

#multiples of 5 between 100 to 200

i=100
l=200
while i<=l:
    if i%5==0:
        print(i)
        i=i+5
print("closed")

#print only multiples of 8 from <user input> to <user input>
i=int(input("enter the first number: "))
l=int(input("enter the second number: "))
while i<=l:
    if i%8==0:
        print(i)
        i=i+8
print("closed")
