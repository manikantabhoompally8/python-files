import mysql.connector
dbconnection = mysql.connector.connect(
host="localhost",
user="root",
database="d12",
password="root123"
)
print("db connected successfully")

tablecreationquery="""
create table if not exists pythontable(
    id int primary key,
    name varchar(50) not null,
    age int,
    email varchar(50) not null unique,
    salary decimal(10,2) not null
)

"""
cursor_=dbconnection.cursor()
# print(cursor_,"cursor")

cursor_.execute(tablecreationquery)
# print("table created successfully")

print("1.add employees")
print("2.read employees")
print("3.update employees")
print("4.delete employees")
print("5.exit")

o=int(input("enter your choice here:..."))
if o==1:
    a=int(input("enter id here:..."))
    b=input("enter name here:...")
    c=input("enter age here:...")
    d=input("enter email here:...")
    e=float(input("enter salary here:...."))
    queryinsertingpythontable="insert into pythontable(id,name,age,email,salary)values (%s,%s,%s,%s,%s)"
    data=(a,b,c,d,e)
    cursor_.execute(queryinsertingpythontable,data)
    print("emp added successfully")
elif o==2:
    pass    



     



