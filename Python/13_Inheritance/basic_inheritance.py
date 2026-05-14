
# The basic of inheritance in Python

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print (f"Name: {self.name}, Age: {self.age}")

class student(person):
    pass


x = student("Akash","22")
x.display()



# the intermiditage inheritance function

class company:
    def __init__(self, comp_name):
        self.comp_name = comp_name

    def company_info(self):
        print(f"Company Name is {self.comp_name}")

class employee(company):
    def __init__(self, emp_name, comp_name) :
        self.emp_name = emp_name
        self.comp_name = comp_name

    def emp_info(self):
        print(f"Employee Name is {self.emp_name}")

    def company_info_child(self):
        print("This is running from employee")
        company.company_info(self)

emp1 = employee("Akash","Google")
emp1.emp_info()
emp1.company_info_child()