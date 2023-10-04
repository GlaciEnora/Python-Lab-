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

    def retsal(self):
        return self.__salary
    
    def display(self):
        print("Name: ", self.name, "\nID: ", self.emp_id, "\nDesignation: ", self.designation)

def calculate(emp, da, hra, pf):
    grosssal = emp.retsal()*(1+(da+hra)/100)
    netsal = emp.retsal()*(1+(da+hra-pf)/100)
    print("Gross salary: ", grossal)
    print("Net salary: ", netsal)


obj = Employee()
obj.getdetail()
da = float(input("DA: "))
hra = float(input("HRA: "))
pf = float(input("PF: "))
obj.display()
calculate(obj, da, hra, pf)
