class EB_Amount:
    def __init__(self):
        self.units_used = 0
        self.bill = 0

    def inputdetail(self):
        self.units_used = int(input("Enter the number of units consumed: "))

    def calc(self):
        if self.units_used <= 200:
            self.bill = 3*self.units_used
        elif 200 < self.units_used <= 500:
            self.bill = 4*self.units_used
        else:
            self.bill = 5.5*self.units_used

    def print(self):
        print("Units consumed: ", self.units_used, "\nBill Amount: ", self.bill)


obj = EB_Amount()
obj.inputdetail()
obj.calc()
obj.print()
