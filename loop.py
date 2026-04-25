# vowels
text="python"
count=0
for i in text:
    if i in "aeiou":
        count=count+1 #count+=1
print("vowels:",count)   
    
#reverse the text
text = "hello"
reverse = ""

for ch in text:
   reverse = ch + reverse

print("Reversed:", reverse)

#palandrome
word="malayaam"
reverse=""
for i in word:
    reverse=i+reverse
if word==reverse:
   print("palandrome")
else:
    print("not palandrome")

count
x="apple"
count=0
for i in x:
     count=count+1
     print(i)


# occurance of each character
text = "apple"
freq = {}

for i in text:
   if i in freq:
       freq[i] += 1
   else:
       freq[i] = 1
print(freq)


# count nom of words
word="manikanta"
words=word.split()
count = 0 
for i in words:
    count+=1
print("word count:",count)

#using for loop to print noms asc dsc

for i in range(-1,-100,-1):
    print(i)
for i in range(1,100):
    print(i)
for i in range(-100,-1,1):
    print(i)
for i in range(100,1,-1):
    print(i)

#while loop 
i=1
while i <=5:
    print(i)
    i+=1

i=1
even=0
while i <=10:
    if i % 2==0:
        even+=1
        print(i)
    i+=1
print("even sum:",even)
 
i=1
odd=0
while i <=10:
    if i % 2!=0:
        odd+=1
        print(i)
    i+=1
print("odd sum:","odd")

#sum of list
numbers=[1,2,3,4,5]
max=max(numbers)
print("sum:",max)

numbers = [1,2,3,4,5]
total = 0

for i in numbers:
   total += i

print("Sum:", total)

numbers=[10,29,30]
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i

print(largest)     


#count even noms
num=[1,2,3,4,5,6,7,8,9]
count=0
for i in num:
    if i%2==0:
        count+=1
print("count:",count)        


#remove dublicatess

num=[1,2,3,3,4,5,6,6,7,8,9,9,0]
unique=[]
for i in num:
    if i not in unique:
        unique.append(i)
print(unique)  
     
numbers=[1,2,4,4,4,5,5,]
freq={}
for i in numbers:
     if i in freq:
          freq[i]+=1
     else:
          freq[i]=1
print(freq)

data={
    "id":26,
    "name":"mani",
    "loc":"HYD"
}
for key,values in data.items():
    print(key,":",values)

student = {"name": "Ram", "age": 20, "marks": 85}
count = 0

for key in student:
   count += 1

print("Total items:", count)










student = {"name": "Ram", "age": 20}

age = "age"

if age in student:
   print("Key exists")
else:
   print("Key not found")





