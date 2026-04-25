age=18
if age>=18:
    print("you can vote")

age=18
if age>=18:
    print("adult")
else:
    print("not adult")    

marks=int(input("enter your marks"))
if marks >= 90:
    print("grade A")
elif marks >=75:
    print("grade B")
else:
    print("pass")
        
a=int(input("enter any nom"))
b=int(input("enter any nom"))
c=int(input("enter any nom"))
max_nom=max(a,b,c)
if a==max_nom:
    print("max nom a")
elif b== max_nom:
    print("max nom is b")
else:
    print("max nom is c")      



username="vamshi"
password="123456"
q=input("enter username: ")
s=input("enter your password: ")
if q=="vamshi" and s=="123456":  
    print("login succesful")
else:
    print("invalid")  

number=int(input("enter any nom:   "))

if number % 3 == 0 :
    print("multiple of 3")

elif number%5==0:
    print("mulltiple of 5")
else:
    print("no multiples of 3&5")        

    num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Multiple of both 3 and 5")
else:
    print("Not a multiple of both 3 and 5")

nom=int(input("enter a number"))
if nom%5==0:
    print("dividible of 5")
else:
    print("not divisible")    


nom=int(input("enter nom:   "))
if (nom%100!=0 and nom%4==0) or (nom%400==0):
      print("leap year")
else:
    print("not leap")


nom=int(input("enter any nom: "))
if nom>=18:
    print("eligible to vote")
else:
    print("not eligible")    


marks=int(input("enter your marks: "))
if marks>=85:
    print("excellent")
elif marks<85 and marks>=70: 
    print("good")
elif marks<=50 and marks>=69:
    print("avg")
else:
    print("fail")       



maths=int(input("Enter maths subj marks here:"))
science=int(input("Enter science subj marks here:"))
english=int(input("Enter english subj marks here:"))
max_marks=max(maths,science,english)
if maths==science==english:
    print("all subs marks are equal")
else:
    if maths==max_marks:
        print("highest marksis maths:",max_marks)
    if science==max_marks:
        print("highest marks is science:",max_marks)
    if english==max_marks:
        print("highest marks is english:",max_marks)

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



