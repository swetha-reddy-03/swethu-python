import random
#create options for playing game
lis = ["stone","paper","scissor"]
#assign the random values to system
system=random.choice(lis)
val=False
count=0
while val==False:
    val=input("Enter the value: ")
    count=count+1
    if val==system:
        print(" Match Tie")
    elif val=="stone":
        if system=="paper":
            print("system won the game")
        else:
            print("you won the game")
    elif val=="paper":
        if system=="scissor":
            print("system won the game")
        else:
            print("you won the game")
    elif val=="scissor":
        if system=="stone":
            print("system won the game")
        else:
            print("you won the game")

    if (count==10):
        print("Exit")
        break
    val= False
    system=random.choice(lis)
                
