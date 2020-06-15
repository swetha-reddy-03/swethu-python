#check a string is palindrome or not using function
def palindrome(a):
    return a[::-1]
b=input("Enter the string: ")
if palindrome(b)==b:
    print("the string is palindrome")
else:
    print("the string is not palindrome")


#check a number is odd or even using function

def odd_even(a):
    return(a)
b=int(input("Enter the number: "))
if odd_even(b)%2==0:
    print("The number is even")
else:
    print("The number is odd")

#check a number is positive or negative using function

def posi_nega(a):
    return(a)
b=int(input("Enter the number: "))
if posi_nega(b)>0:
    print("The number is positve")
else:
    print("The number is negative")

#get two numbers from user and do operation (a+b)(a-b)

def multi_two(a,b):
    return(a,b)
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
print(multi_two(a,b))

#get three numbers from user and do opertion (a+b)(a-b)(a-c)

def multi_three(a,b,c):
    return(a,b,c)
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
print((multi_three(a,b,c))

#check the number prime or not using functions

def find_factors(n):
    count=0
    for i in range(2,(n//2+1)):
        if(n%i==0):
            count=count+1
        return count
n=int(input("Enter the number: "))
x=find_factors(n)
if(x==0 and n!=1):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")


#check the number is armstrong or not using function
def Armstrong_Number(Num):
           Sum = 0
           Dig = 0

           Temp = Num
           while Temp > 0:
                      Dig = Dig + 1
                      Temp = Temp // 10

           Temp = Num
           for n in range(1, Temp + 1):
                      Rem = Temp % 10
                      Sum = Sum + (Rem ** Dig)
                      Temp //= 10
           return Sum
Num = int(input("Enter the number: "))

if (Num == Armstrong_Number(Num)):
    print(Num,"is armstrong number")
else:
    print(Num,"is not armstrong number")


#fabonacci series using functions
def fabonacci_series(num):
    return(num)
num=int(input("enter the number"))
first_value=0
second_value=1
for n in range(0,num):
    if(n<=1):
        next=n
    else:
        next=first_value+second_value
        first_value=second_value
        second_value=next
    print(next)



