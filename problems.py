#largestnumss
nums=[1,2,2,3,4,5,6,7,8,9]
unique_num=list(set(nums))
print(unique_num)
unique_num.sort()
secondlargest=unique_num[-1]
print("secondlargest:",secondlargest)

#palandrome

name=input("enter any input")
rev=""
for i in name:
    rev=i+rev
#  datatypes\conditional.py
if name==rev:
    print("p")
else:
    print("n")    
    # C:\Users\bhoom\OneDrive\Desktop\mani python\datatypes
   
