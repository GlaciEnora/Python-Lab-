class badOperand(Exception):
    def __init__(self):
        super().__init__("Not a Valid Operand")

class badOperator(Exception):
    def __init__(self):
        super().__init__("Not a valid Operator")

class Operand:
    def __init__(self):
        self._opnd1 = 0
        self._opnd2 = 0

    def getdata(self):
        self.opnd1 = int(input("Enter the first operand: "))
        self.opnd2 = int(input("Enter the second operand: "))

class Operator:
    def __init__(self):
        self.opr = ""

    def getdata(self):
        self.opr = input("Enter the operator: ")

class Operation(Operand, Operator):
    def __init__(self):
        self.res = 0
        Operand.__init__(self)
        Operator.__init__(self)
        Operand.getdata(self)
        super(Operand, self).getdata()

    def calculation(self):
        try:
            if (self.opnd1 not in range(10000, 20001)) and (self.opnd2 not in range(10000, 20001)):
                raise badOperand()
            if self.opr not in ["+", "-", "*", "/", "//", "%", "**"]:
                raise badOperator()
            else:
                self.res = eval( str(self.opnd1) + self.opr + str(self.opnd2))
        except (badOperand, badOperator) as ex:
            print("An exception has occured: ", ex)
        print("The result is: ", self.res)


obj = Operation()
obj.calculation()
        
