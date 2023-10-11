class Employee:
    def __init__(self):
        self._empid = 0
        self._name = ""
        self._desgn = ""
        self._sal = 0

    def getinput(self):
        self._empid = int(input("Enter the employee id: "))
        self._name = input("Enter employee name: ")
        self._desgn = input("Enter designation: ")
        self._sal = int(input("Enter the base salary: "))

class Contract(Employee):
    def __init__(self):
        super().__init__()
        super().getinput()
        self.numHrs = 0
        self.wagesHrs = 0
        
    def getinput(self):
        self.numHrs = int(input("Enter the number of hours clocked: "))
        self.wagesHrs = float(input("Enter the wage per hour: "))
        self._sal = self.numHrs * self.wagesHrs

    def display(self):
        print("Name: ", self._name, "\nID: ", self._empid, "\nDesignation: ", self._desgn, \
              "\nNet salary: ", self._sal)

class Permanent(Employee):
    def __init__(self):
        super().__init__()
        super().getinput()
        self.da = 0
        self.hra = 0
        self.pf = 0

    def getinput(self):
        self.da = float(input("DA: "))
        self.hra = float(input("HRA: "))
        self.pf = float(input("PF: "))
        self._sal *= (1+((self.da + self.hra + self.pf)/100))

    def display(self):
        print("Name: ", self._name, "\nID: ", self._empid, "\nDesignation: ", self._desgn, \
              "\nNet salary: ", self._sal)

obj1 = Contract()
obj1.getinput()
obj1.display()

obj2= Permanent()
obj2.getinput()
obj2.display()
