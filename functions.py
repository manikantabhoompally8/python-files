# def greet(name):
#     print("Hello", name)

# greet("Manikanta")
# def welcome():
#     print("Welcome to Python")

# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)
# def get_number():
#     return 10

# num = get_number()
# print(num)

# #regester
# def register():
#     a=input("enter your name:  ")
#     b=input("enter your email:  ")
#     c=input("enter your password:  " )            
#     cp=input("enter your password:  " )
#     if c==cp:
#         print("reg suc")
#     else:
#         print("reg faileddd")
# register()       

# #loginn
# def login():
#     e="mani@123"
#     p=123
#     a=input("enter your email:  ")
#     b=int(input("enter your password:   "))
#     if e==a and p==b:
#         print("login successful")
#     else:
#         print("login falied")  
# login()   
# x=int(input("enter any nom:  "))
# y=int(input("enter any nom:  "))   
# def abc(x,y):
#     c=x+y
#     print(c)
#     return c
# c=abc(x,y)

# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("mani"))

# def fibanacci(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end="")
#         a,b=b,a+b
# fibanacci(8)       

# def sq(n):
#     print(n*n)
# sq(3)        


nums=[3,4,7,5,3,2,1,4,7,8]
result=[min(nums),max(nums)]
print(result)
