class students:
    school_name="xyz school"
    def set_details(self):
        self.name="mani"
        self.marks=85
    def display(self):
        print(self.name,self.marks,self.school_name)

o=students()
o.set_details()
o.display()





class employee:
    company="infosys"
    def set_data(self):
        self.name="ravi"
        self.salary=2000
    def inc_salary(self):
        self.salary=self.salary+500
    def display(self): 
        print(self.name,self.salary,self.company)
o=employee()
o.set_data()
o.inc_salary()
o.display()


class mobiles:
    brand="apple"
    def set_details(self):
        self.model="iphone 15"
        self.price=80000
    def discount(self):
        self.price=self.price-(self.price*10/100)
    def display(self):
    
        print(self.model,self.price,self.brand)  
o=mobiles()
o.set_details()
o.discount()
o.display()
