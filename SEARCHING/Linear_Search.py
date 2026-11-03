
target=int(input("enter the target:"))
array=[1,2,344,223,654,00,-13,54]
found=0
for i in range(0,len(array)):
    if array[i]==target:
        print("the target is found at index:",i)
        found=1
if found==0:
    print("The target is not in the array.")
