#PROGRAM-1
#check wether the number is prime or not
#prime ==>only divisible by 1 and itself

n = int(input("Enter a number: "))
for i in range(2,n-1):
    if n % i == 0:
        print(n,"not a prime number")
        break
else: 
    print(n,"prime number")
print("closed")


#PROGRAM-2
#check the list of prime numbers with in a range
 
x = int(input("Enter the first Value: "))
y = int(input("Enter the second Value: "))
for num in range(x , y+1):
    count = 0
    for i in range(2,(num//2+1)):
        if (num %i == 0):
            count = count + 1
            break
    if(count == 0 and num != 1):
        print(num)
print("above are the list of prime numbers")

#PROGRAM-3
#check whether the num is Armstrong or not

num=int(input("Enter the number: "))

#initializing the sum and number of digits
sum=0
dig=0

temp=num
while temp>0:
    dig=dig+1
    temp=temp//10
temp=num
for n in range (1,temp+1):
    rem=temp%10
    sum=sum+(rem**dig)
    temp//=10
if num==sum:
    print(num,"is armstrong number")
else:
    print(num,"is not an armstrong number")
print("closed")


#PROGRAM-4
#print list of armstrong numbers with in range
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
for num in range(x,y+1):
    sum=0
    dig=0
    temp=num
    while temp>0:
        dig=dig+1
        temp=temp//10
    temp=num
    for n in range (1,temp+1):
        rem=temp%10
        sum=sum+(rem**dig)
        temp//=10
    if num==sum:
        print(num)
print("Above are the list of armstrong numbers")


#PROGRAM-5
#find the sum of digits
#check the sum of digits is even or odd
num=int(input("Enter the number: "))
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
if(sum%2==0):
    print("sum of digits number is even")
else:
    print("sum of digits number is odd")


#PROGRAM-6
#find the product of digits
a= int(input("Enter the number: "))
product=1
a=int(str(a).replace("0","1"))
for num in str(a):
    product=product*int(num)
    print(product)

#PROGRAM 11
#find the factors of a number
 
number = int(input("Enter the Number: "))

print("Factors of a Given Number {0} are:".format(number))

for value in range(1, number + 1):
    if(number%value == 0):
        print("{0}".format(value))


#PROGRAM 12
#fibonacci series
Number = int(input("\nPlease Enter the Range Number: "))

First_Value = 0
Second_Value = 1
        
for Num in range(0, Number):
           if(Num <= 1):
                      Next = Num
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next)




            
