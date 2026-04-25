# arthimetic operator
a = 10
b = 3

print(a + b)   
print(a - b)  
print(a * b)   
print(a / b)   
print(a % b)   
print(a ** b)  
print(a // b)  
a = 10
b = 5
# comparision operator
print(a == b)   
print(a != b)   
print(a > b)   
print(a < b)    
print(a >= b)  
print(a <= b)   
# logical
a=True
b=False
print(a and b)
print(a or b)
print(not b)
#membership operator
list1 = [1, 2, 3, 4]

print(2 in list1)      
print(5 not in list1)

name="mani"
print("p" in name)
print("i" in name)
data={"name":"mani","age":28}
print("name" in data)
print("ram" in data)
#assignment
cart=0
cart=cart+1
print(cart)  
cart=10
cart=cart-1
print(cart)  
x=10
x+=5
print(x)
x-=4
print(x)
x*=3
print(x)
x/=3
print(x)
x//=3
print(x)
x%=7
print(x)
x=10
x**=3
print(x)


#calculator prgmd
a=int(input("enter any nom: "))
b=int(input("enter any nom: "))
operators=input("enter operator(+,*,-,/):")
if operators=="+":
    print(a+b)
elif operators=="*":
     print(a*b)
elif operators=="/":
     print(a/b)

elif operators=="-":
     print(a-b)