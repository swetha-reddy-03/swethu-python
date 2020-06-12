n=int(input("enter the num: "))
if n>=0 and n<=100:
    print("valid")
if n>=90 and n<=99:
    print("grade a")
elif n>=80 and n<=89:
    print("grade b")
elif n>=70 and n<=79:
    print("grade c")
elif n>=60 and n<=69:
    print("grade d")
elif n>=50 and n<=59:
    print("grade e")
elif n>=0 and n<=49:
    print("grade fail")
else:
    print("in valid")


