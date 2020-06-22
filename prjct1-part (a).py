#program for data structure and data type calculator
print("Welcome to Data structure or Data type calculator")

print("Options are : \n"
      "1.Numbers \n"
      "2.String \n"
      "3.List \n"
      "4.Tuple \n"
      "5.Dictionary \n"
      "6.Set \n"
      "7.Data structure")

while True:
    user=int(input("select the option : "))
             
    if user==1:
        choice='Numbers'
    elif user==2:
        choice='String'
    elif user==3:
        choice='List'
    elif user==4:
        choice='Tuple'
    elif user==5:
        choice='Dictionary'
    elif user==6:
        choice='Set'
    elif user==7:
        choice='Data structure'
    else:
        print("In valid")
        
    print("user choice is : " + choice)
    
#operations in Numbers
    
    if user==1:
        print("welcome to Numbers")
        print("The Numbers operations are : \n"
              "1. Addition \n"
              "2. Multiplication \n"
              "3. Subtraction \n"
              "4. Division \n"
              "5. Modulus \n"
              "6. Exponential \n"
              "7. Floor division \n"
              "8. equals to \n"
              "9. not equals to \n"
              "10. greaterthan \n"
              "11. graterthan or equalsto \n"
              "12. lessthan \n"
              "13. lessthan or equalsto \n"
              "14. int \n"
              "15. float \n"
              "16. Fibonacci \n"
              "17. Go to the main menu \n"
              "18. Exit from the program \n")
        
        user_numbers=int(input("select the operation in numbers : "))

        #conditions for doing operations in numbers

        #Doing addition operation
        if user_numbers==1:
            print("Welcome to Addition operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            num3=num1+num2
            print(num3)
            
        #conditions for multiplication operation
            
        elif user_numbers==2:
            print("Welcome to Multiplication operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            num3=num1*num2
            print(num3)
            
        #conditions for substraction operation
            
        elif user_numbers==3:
            print("Welcome to subtraction operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            num3=num1-num2
            print(num3)
            
        #conditions for division operation
            
        elif user_numbers==4:
            print("Welcome to Division operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            num3=num1/num2
            print(num3)

        #conditions for Modulus operation
            
        elif user_numbers==5:
            print("Welcome to Modulus operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            num3=num1%num2
            print(num3)

        #conditions for Exponential operation
            
        elif user_numbers==6:
            print("Welcome to Exponential operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            num3=num1**num2
            print(num3)

        #conditions for floordivision operation
            
        elif user_numbers==7:
            print("Welcome to Floor division operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            num3=num1//num2
            print(num3)

        #conditions for equals to operation
            
        elif user_numbers==8:
            print("Welcome to equalsto operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            print(num1==num2)

        #conditions for not equals to operation
            
        elif user_numbers==9:
            print("Welcome to not equals to operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            print(num1!=num2)

        #conditions for greaterthan operation
            
        elif user_numbers==10:
            print("Welcome to greaterthan operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            print(num1>num2)

        #conditions for greaterthan or equalsto operation
            
        elif user_numbers==11:
            print("Welcome to greaterthan or equalsto operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            print(num1>=num2)

        #conditions for lessthan operation
            
        elif user_numbers==12:
            print("Welcome to lessthan operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            print(num1<num2)

        #conditions for lessthan or equals to operation
            
        elif user_numbers==13:
            print("Welcome to lessthan or equals to operation")
            num1=int(input("Enter the first number : "))
            num2=int(input("Enter the second number : "))
            print(num1<=num2)

        #conditions for check given value is integer or not
           
        elif user_numbers==14:
            print("check given value is integer or not")
            num=int(input("Enter the number : "))
            print(type(num))
             
        #conditions for check given value is float or not
            
        elif user_numbers==15:
            print("check given value is float or not")
            num=float(input("Enter the number : "))
            print(type(num))

        #conditions for fibonacci operation
            
        elif user_numbers==16:
            number_choice='fibonacci'
            print("Welcome to Fibonacci")
            
            Number = int(input("Enter the Range Number: "))
            i = 0
            First_Value = 0
            Second_Value = 1
            while(i < Number):
                if(i <= 1):
                    Next = i
                else:
                    Next = First_Value + Second_Value
                    First_Value = Second_Value
                    Second_Value = Next
                print(Next)
                i = i + 1
                
        #conditions for go to the main menu
                
        elif user_numbers==17:
            number_choice='Go to the main menu'
            print(user)

        #conditions for Exit from the program
            
        elif user_numbers==18:
            number_choice='Exit from the program'
            print("Exit from the program")
        else:
            print("In valid")
        break

    #Operations in string
    
    if user==2:
        print("Welcome to String")
        print("The String operations are : \n"
              "1. capitalize \n"
              "2. count \n"
              "3. find \n"
              "4. cooncatenation \n"
              "5. index \n"
              "6. upper \n"
              "7. lower \n"
              "8. isalpha \n"
              "9. join \n"
              "10. split \n"
              "11. replace \n"
              "12. swapcase \n"
              "13. tittle \n"
              "14. strip \n"
              "15. len \n")
        
        user_string=int(input("select the any above string operations : " ))

        #conditions for doing string operations

        #conditions for capitalize operation in string

        if user_string==1:
            print("Welcome to capitalize operation")
            str=input("Enter the string : ")
            s=str.capitalize()
            print(s)

        #conditions for count operation in string
            
        elif user_string==2:
            print("Welcome to count operation")
            str=input("Enter the string : ")
            x=input("Enter the substring to check the str : ")
            y=str.count(x)
            print(y)

        #conditions for find operation in string
            
        elif user_string==3:
            print("Welcome to find operation")
            str=input("Enter the string : ")
            x=input("Enter the substring to find the str : ")
            y=str.find(x)
            print(y)

        #conditions for concatenation operation in string
            
        elif user_string==4:
            print("Welcome to format operation")
            
            str1=input("Enter the first string : ")
            str2=input("Enter the second string : ")
            x=str1+str2
            print(x)

        #conditions for index operation in string
            
        elif user_string==5:
            print("Welcome to index operation")
            str=input("Enter the string : ")
            x=input("Enter the substring to index the str : ")
            y=str.index(x)
            print(y)

        #conditions for upper operation in string
            
        elif user_string==6:
            print("Welcome to upper operation")
            str=input("Enter the string : ")
            x=str.upper()
            print(x)

        #conditions for lower operation in string
            
        elif user_string==7:
            print("Welcome to lower operation")
            str=input("Enter the string : ")
            x=str.lower()
            print(x)

        #conditions for isalpha operation in string
            
        elif user_string==8:
            print("Welcome to isalpha operation")
            str=input("Enter the string : ")
            x=str.isalpha()
            print(x)

        #conditions for join operation in string
            
        elif user_string==9:
            print("Welcome to join operation")
            str=input("Enter the string : ")
            x="#".join(str)
            print(x)

        #conditions for split operation in string
            
        elif user_string==10:
            print("Welcome to split operation")
            str=input("Enter the string : ")
            x=str.split()
            print(x)

        #conditions for replace operation in string
            
        elif user_string==11:
            print("Welcome to replace operation")
            str=input("Enter the string : ")
            x=input("Enter the value want to replace : ")
            y=input("Enter the value want to replaced by : ")
            z=str.replace(x,y)
            print(z)

        #conditions for swapcase operation in string
            
        elif user_string==12:
            print("Welcome to swapcase operation")
            str=input("Enter the string : ")
            x=str.swapcase()
            print(x)

        #conditions for title operation in string
            
        elif user_string==13:
            print("Welcome to tittle operation")
            str=input("Enter the string : ")
            x=str.tittle()
            print(x)

        #conditions for strip operation in string
            
        elif user_string==14:
            print("Welcome to strip operation")
            str=input("Enter the string : ")
            x=input("Enter the substring to strip the str : ")
            y=str.strip()
            print(str,x)

        #conditions for length operation in string
            
        elif user_string==15:
            print("Welcome to length operation")
            str=input("Enter the number : ")
            x=len(str)
            print("length of the string : ",x)
        else:
            print("In valid")
        break

    #operations in List
    
    if user==3:
        print("Welcome to the List")
        print("The List operations are : \n"
              "1. concatenation \n"
              "2. multiplication \n"
              "3. append \n"
              "4. insert \n"
              "5. remove \n"
              "6. pop \n"
              "7. clear \n"
              "8. extend \n"
              "9. index \n"
              "10. count \n"
              "11. del \n"
              "12. copy \n"
              "13. reverse \n"
              "14. len \n"
              "15. sort \n")

        user_list=int(input("select any above List operation : "))

        #conditions for doing operation in List

        #conditions for concatenation operation in list
        
        if user_list==1:
            print("Welcome to concatenation operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            li2=int(input("Enter no of elements in list : "))
            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(li1):
                va1=int(input("Enter element no" + str(i)))
                Dyn_list1.append(va1)
            print(Dyn_list1)
            
            for j in range(li2):
                va2=int(input("Enter element no" + str(j)))
                Dyn_list2.append(va2)
            print(Dyn_list2)
            
            print(Dyn_list1+Dyn_list2)

        #conditions for multiplication operation in list
            
        elif user_list==2:
            print("Welcome to multiplication operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)

            multi=int(input("Enter the multiply number : "))
            print(Dyn_list*multi)
            
        #conditions for append operation in list
            
        elif user_list==3:
            print("Welcome to append operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)

            x=int(input("Enter the append number : "))
            Dyn_list.append(x)
            print(Dyn_list)

        #conditions for append operation in list
            
        elif user_list==4:
            print("Welcome to insert operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)

            x=int(input("Enter the value first want to insert: "))
            y=int(input("Enter the value second want to insert: "))
            Dyn_list.insert(x,y)
            print(Dyn_list)

        #conditions for remove operation in list
            
        elif user_list==5:
            print("Welcome to remove operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)

            x=int(input("Enter the remove number : "))
            Dyn_list.remove(x)
            print(Dyn_list)

        #conditions for pop operation in list
            
        elif user_list==6:
            print("Welcome to pop operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)

            x=int(input("Enter the pop number : "))
            Dyn_list.pop(x)
            print(Dyn_list)

        #conditions for clear operation in list
        elif user_list==7:
            print("Welcome to clear operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)
            
            Dyn_list.clear()
            print(Dyn_list)

        #conditions for extend operation in list
        elif user_list==8:
            print("Welcome to extend operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            li2=int(input("Enter no of elements in list : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(li1):
                va1=int(input("Enter element no" + str(i)))
                Dyn_list1.append(va1)
            print(Dyn_list1)

            for j in range(li2):
                va2=int(input("Enter element no" + str(j)))
                Dyn_list2.append(va2)
            print(Dyn_list2)
            
            Dyn_list1.extend(Dyn_list2)
            print(Dyn_list1)

        #conditions for index operation in list
            
        elif user_list==9:
            print("Welcome to index operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)

            x=int(input("check the index of number : "))
            li2=Dyn_list.index(x)
            print(li2)

        #conditions for count operation in list
            
        elif user_list==10:
            print("Welcome to count operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)

            x=int(input("Enter the number want to count : "))
            li2=Dyn_list.count(x)
            print(li2)

        #conditions for del operation in list
            
        elif user_list==11:
            print("Welcome to del operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)
            
            del Dyn_list
            print(Dyn_list)

        #conditions for copy operation in list
            
        elif user_list==12:
            print("Welcome to copy operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)
            
            li2=Dyn_list.copy()
            print(li2)

        #conditions for reverse operation in list
            
        elif user_list==13:
            print("Welcome to reverse operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)
            
            Dyn_list.reverse()
            print(Dyn_list)

        #conditions for length operation in list
            
        elif user_list==14:
            print("Welcome to length operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)
            
            li2=len(Dyn_list)
            print(li2)

        #conditions for sort operation in list
            
        elif user_list==15:
            print("Welcome to sort operation in List")
            
            li1=int(input("Enter no of elements in list : "))
            Dyn_list=[]
            for i in range(li1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
            print(Dyn_list)
            
            Dyn_list.sort()
            print(Dyn_list)
            
        else:
            print("In valid")
        break
    #operations in Tuple
    
    if user==4:
        print("Welcome to Tuple")
        print("The Tuple operations are : \n"
              "1. len \n"
              "2. index \n"
              "3. count \n"
              "4. join \n"
              "5. remove \n")
        
        user_tuple=int(input("select any above Tuple operation : "))
        #conditions of doing operations in tuple

        #condition for length operation in tuple
        
        if user_tuple==1:
            print("Welcome to length operation in Tuple")
            
            tup=int(input("Enter no of elements in Tuple : "))
            Dyn_list=[]
            for i in range(tup):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                
            x=tuple(Dyn_list)
            print(x)
            print(len(x))
            
        #condition for index operation in tuple
            
        elif user_tuple==2:
            print("Welcome to index operation in Tuple")
            
            tup1=int(input("Enter no of elements in Tuple : "))
            Dyn_list=[]
            for i in range(tup1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                
            tup2=tuple(Dyn_list)
            print(tup2)
            
            x=int(input("Enter the number want to check index : "))
            print(tup2.index(x))

        #condition for count operation in tuple
            
        elif user_tuple==3:
            print("Welcome to count operation in Tuple")
            
            tup1=int(input("Enter no of elements in Tuple : "))
            Dyn_list=[]
            for i in range(tup1):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                
            tup2=tuple(Dyn_list)
            print(tup2)
            
            x=int(input("Enter the number want to check index : "))

            tup3=tup2.count(x)
            print(tup3)

        #condition for join operation in tuple
            
        elif user_tuple==4:
            print("Welcome to join operation in Tuple")
            
            tup1=int(input("Enter no of elements in first Tuple : "))
            tup2=int(input("Enter no of elements in second Tuple : "))
            
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(tup1):
                va1=int(input("Enter first tuple no" + str(i)))
                Dyn_list1.append(va1)
                
            tup3=tuple(Dyn_list1)
            print(tup3)

            for j in range(tup2):
                va2=int(input("Enter second tuple no" + str(j)))
                Dyn_list2.append(va2)
                
            tup4=tuple(Dyn_list2)
            print(tup4)
            
            x=tup3+tup4
            print(x)

        #condition for remove operation in tuple
            
        elif user_tuple==5:
            print("Welcome to remove operation in Tuple")
            
            tup=int(input("Enter no of elements in Tuple : "))
            Dyn_list=[]
            for i in range(tup):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                
            x=tuple(Dyn_list)
            print(x)
            
            del x
            print(x)
            
        else:
            print("In valid")
        break

    #operations of Dictionary
    if user==5:
        print("Welcome to Dictionary")
        print("The Dictionary operations are : \n"
              "1. clear \n"
              "2. copy \n"
              "3. len \n"
              "4. get \n"
              "5. items \n"
              "6. keys \n"
              "7. pop \n"
              "8. popitem \n"
              "9. update \n"
              "10. values \n")
        
        user_dic=int(input("select any one of dictionary operations : "))

        #conditions for doing operations in Dictionary

        #conditions for clear operation in dictionary
        if user_dic==1:
            print("Welcome to clear operation in dictionary")
            
            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)
            
            new_dict.clear()
            print(new_dict)

        #conditions for copy operation in dictionary
            
        elif user_dic==2:
            print("Welcome to copy operation in dictionary")

            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)
            
            x=new_dict.copy()
            print(x)

        #conditions for length operation in dictionary
            
        elif user_dic==3:
            print("Welcome to fromkeys operation in dictionary")

            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)
            
            z=len(new_dict)
            print(z)
                                  
        #conditions for get operation in dictionary
            
        elif user_dic==4:
            print("Welcome to get operation in dictionary")

            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)

            d=int(input("Enter the item u want to get:"))
            z=new_dict.get(d)
            print(z)
            

        #conditions for items operation in dictionary
            
        elif user_dic==5:
            print("Welcome to items operation in dictionary")
            
            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)
            
            z=new_dict.items()
            print(z)

        #conditions for key operation in dictionary
            
        elif user_dic==6:
            print("Welcome to key operation in dictionary")

            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)
            
            new_dict.clear()
            print(new_dict)
            
            z=new_dict.keys()
            print(z)

        #conditions for pop operation in dictionary
            
        elif user_dic==7:
            print("Welcome to pop operation in dictionary")

            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)
            
            p=int(input("Enter the item u want to pop :"))
            new_dict.pop(p)
            print(new_dict)

        #conditions for popitems operation in dictionary
            
        elif user_dic==8:
            print("Welcome to popitem operation in dictionary")

            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)
            
            new_dict.popitem()
            print(new_dict)

        #conditions for update operation in dictionary
            
        elif user_dic==9:
            print("Welcome to update operation in dictionary")

            #create one dictionary
            list_keys=int(input("Enter no of keys of first dict : "))
            list_values=int(input("Enter no of values of first dict : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys of first dict" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values of first dict" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict1=dict(zip(x,y))
            print(new_dict1)

            #create another dictionary
            list_keys=int(input("Enter no of keys of second dict: "))
            list_values=int(input("Enter no of values of second dict : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys of second dict" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values of second dict" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict2=dict(zip(x,y))
            print(new_dict2)

            #update one dictionary with another dictionary
            new_dict1.update(new_dict2)
            print(new_dict1)

        #conditions for values operation in dictionary
            
        elif user_dic==10:
            print("Welcome to values operation in dictionary")
            list_keys=int(input("Enter no of keys : "))
            list_values=int(input("Enter no of values : "))

            Dyn_list1=[]
            Dyn_list2=[]
            
            for i in range(list_keys):
                va1=int(input("Enter the keys" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                x=set(Dyn_list1)
                print(x)
            
            for j in range(list_values):
                va2=input("Enter values" + str(j))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                y=set(Dyn_list2)
                print(y)
            
            new_dict=dict(zip(x,y))
            print(new_dict)
            
            z=new_dict.values()
            print(z)
            
        else:
            print("In valid")
        break

    #operations in Set
    
    if user==6:
        print("Welcome to Set")
        print("The Set operations are : \n"
              "1. add \n"
              "2. clear \n"
              "3. copy \n"
              "4. pop \n"
              "5. remove \n"
              "6. union \n"
              "7. intersection \n"
              "8. intersection_update \n"
              "9. issubset \n"
              "10. issuperset \n"
              "11. update \n"
              "12. difference \n"
              "13. difference_update \n"
              "14. discard \n"
              "15. symmetric_difference \n")
        
        user_set=int(input("select any one of set operations : "))

        #conditions for add operation set
        
        if user_set==1:
            print("Welcome to add operation in Set")
            
            s=int(input("Enter no of elements in set : "))
            Dyn_list=[]
            for i in range(s):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                print(Dyn_list)
                
            x=set(Dyn_list)
            print(x)

            x=int(input("Enter the element want to add in set : "))
            Dyn_list.add(x)
            print(Dyn_list)
            
         #conditions for clear operation set
            
        elif user_set==2:
            print("Welcome to clear operation in Set")
            
            s=int(input("Enter no of elements in set : "))
            Dyn_list=[]
            for i in range(s):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                print(Dyn_list)
                
            x=set(Dyn_list)
            print(x)
            
            x.clear()
            print(x)

        #conditions for copy operation set
            
        elif user_set==3:
            print("Welcome to copy operation in Set")
            set1={1,2,3,4,5}
            set2=set1.copy()
            print(set2)

        #conditions for pop operation set
            
        elif user_set==4:
            print("Welcome to pop operation in Set")
            
            s=int(input("Enter no of elements in set : "))
            Dyn_list=[]
            for i in range(s):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                print(Dyn_list)
                
            x=set(Dyn_list)
            print(x)
            
            x.pop()
            print(x)

        #conditions for remove operation set
            
        elif user_set==5:
            print("Welcome to remove operation in Set")
            
            s=int(input("Enter no of elements in set : "))
            Dyn_list=[]
            for i in range(s):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                print(Dyn_list)
                
            x=set(Dyn_list)
            print(x)

            y=int(input("Enter the element want to remove in set : "))
            x.remove(y)
            print(x)

        #conditions for union operation set
            
        elif user_set==6:
            print("Welcome to union operation in Set")
            
            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            u=x.union(y)
            print(u)

        #conditions for intersection operation set
            
        elif user_set==7:
            print("Welcome to intersection operation in Set")

            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            z=x.intersection(y)
            print(z)

        #conditions for intersection_update operation set
        elif user_set==8:
            print("Welcome to intersection_update operation in Set")

            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            z=x.intersection_update(y)
            print(Z)

        #conditions for issubset operation set
            
        elif user_set==9:
            print("Welcome to issubset operation in Set")
            
            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            z=x.issubset(y)
            print(z)

        #conditions for issuperset operation set
            
        elif user_set==10:
            print("Welcome to issuperset operation in Set")

            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            z=x.issuperset(y)
            print(z)

        #conditions for update operation set
            
        elif user_set==11:
            print("Welcome to update operation in Set")

            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            x.update(y)
            print(x)

        #conditions for difference operation set
            
        elif user_set==12:
            print("Welcome to difference operation in Set")
            
            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            z=x.difference(y)
            print(z)

        #conditions for difference_update operation set
            
        elif user_set==13:
            print("Welcome to difference_update operation in Set")
            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            z=x.difference_update(y)
            print(z)

        #conditions for discard operation set
            
        elif user_set==14:
            print("Welcome to discard operation in Set")

            s=int(input("Enter no of elements in set : "))
            Dyn_list=[]
            for i in range(s):
                val=int(input("Enter element no" + str(i)))
                Dyn_list.append(val)
                print(Dyn_list)
                
            x=set(Dyn_list)
            print(x)

            y=int(input("Enter the element want to discard : "))
            x.discard(y)
            print(x)

        #conditions for symmetric_difference operation set
            
        elif user_set==15:
            print("Welcome to symmetric_difference operation in Set")

            s1=int(input("Enter no of elements in set1 : "))
            s2=int(input("Enter no of elements in set2 : "))
            Dyn_list1=[]
            Dyn_list2=[]
            for i in range(s1):
                va1=int(input("Enter element in set1 no" + str(i)))
                Dyn_list1.append(va1)
                print(Dyn_list1)
                
            x=set(Dyn_list1)
            print(x)
            
            for j in range(s2):
                va2=int(input("Enter element in set2 no" + str(j)))
                Dyn_list2.append(va2)
                print(Dyn_list2)
                
            y=set(Dyn_list2)
            print(y)
            
            z=x.symmetric_difference(y)
            prin(z)
            
        else:
            print("In valid")
        break
        
            
        
            
        
            
              
              
        
             
            
    
            
            
            
            
        
        
                     
                     
