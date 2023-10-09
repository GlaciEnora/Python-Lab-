class Employee:
    emp_id = 0
    name = ""
    designation = ""

    def __init__(self):
        self.__salary = 0

    def getdetail(self):
        self.emp_id = int(input("Enter the employee id: "))
        self.name = input("Enter employee name: ")
        self.designation = input("Enter employee designation: ")
        self.__salary = int(input("Enter the salary: "))

    def get_sal(self):
        return self.__salary
    
    def set_sal(self, a):
        self.__salary = a

    def display(self):
        print("Name: ", self.name, "\nID: ", self.emp_id, "\nDesignation: ", self.designation)

    salary = property(get_sal, set_sal)

def calculate(emp, da, hra, pf):
    emp.salary *= (1+(da+hra)/100)
    print("Gross salary: ", emp.salary)
    emp.salary *= (1+(da+hra-pf)/100)
    print("Net salary: ", emp.salary)

obj = Employee()
obj.getdetail()
da = float(input("DA: "))
hra = float(input("HRA: "))
pf = float(input("PF: "))
obj.display()
calculate(obj, da, hra, pf)
