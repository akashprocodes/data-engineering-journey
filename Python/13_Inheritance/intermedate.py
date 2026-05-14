
# The intermiditage inheritance function

class company:
    def __init__(self, comp_name):
        self.comp_name = comp_name

    def company_info(self):
        print(f"Company Name is {self.comp_name}")

class country:
    def __init__(self, country_name):
        self.country_name = country_name

    def country_info(self):
        print(f"Country Name is {self.country_name}")
        

class employee(company, country):
    def __init__(self, emp_name, comp_name , country_name) :
        self.emp_name = emp_name
        self.comp_name = comp_name

        country.__init__(self, country_name)

    def emp_info(self):
        print(f"Employee Name is {self.emp_name} from {self.country_name}")

    def company_info_child(self):
        print("This is running from employee")
        company.company_info(self)

emp1 = employee("Akash","Google", "india")
emp1.emp_info()
emp1.company_info_child()