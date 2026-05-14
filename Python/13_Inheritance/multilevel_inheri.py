
#  Multilevel Inheritance in python

class company:                         #first class
    def __init__(self, comp_name):
        self.comp_name = comp_name

    def company_info(self):
        print(f"Company Name is {self.comp_name}")

class department(company):              #second class inheriting first class
    def __init__(self, department_name, comp_name):
        self.department_name = department_name
        company.__init__(self, comp_name)

    def department_info(self):
        print(f"Department Name is {self.department_name} of {self.comp_name}")

class employee(department):     #third class inheriting first and second class
    def __init__(self, emp_name, comp_name , department_name) :
        self.emp_name = emp_name
        department.__init__(self, department_name, comp_name)

    def All_info(self):
        print(f"Employee Name is {self.emp_name} from {self.comp_name} works in {self.department_name} department.")

    
emp1 = employee("Akash","wipro","Data-engineering")
emp1.company_info()
emp1.department_info()
emp1.All_info()