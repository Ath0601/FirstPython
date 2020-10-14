list1= []
list2= []
n=1
print("Enter numbers for list")
while n<=5:
    x= int(input())
    list1.append(x)
    if x>0:
        list2.append(x)
    n+=1
print("The positive numbers in the list are", list2)
