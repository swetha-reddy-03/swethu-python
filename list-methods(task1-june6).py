#create a empty list
list1=[]
#concatenate empty list1 with another list
list2=list1+[5,6,8,9]
print(list2)
#add elements to list1
list3=list1+[8,9,1,5,6,7,8]
print(list3)
#find no.of occurence of 8
x=list3.count(8)
print(x)
#find average of list
avg=sum(list3)//len(list3)
print("avg of the list: ",avg)
#find sum + min ele + max ele
z=sum(list3)+min(list3)+max(list3)
print(z)
#find mean and median of list
mean= sum(list3)//len(list3)
print("mean of the list: ",mean)

list3.sort()
median=list3[len(list3)//2]
print("median of the list: ",median)
#remove duplicates in concatenated list and give out in tuple format
print(list(set(list3)))
