class Distance:
    def __init__(self):
        self.feet = 0
        self.inches = 0

    def getinput(self):
        self.feet = float(input("Enter the feet: "))
        self.inches = float(input("Enter the inches: "))
        if self.inches >= 12:
            self.inches -= 12
            self.feet += 1

class MTRDistance(Distance):
    ftm = 0.3048
    
    def __init__(self):
        super().__init__()
        super().getinput()
        self.mtrs = 0
        self.cms = 0
        
    def getinput(self):
        self.mtrs = self.feet * self.ftm
        self.cms = self.inches * 2.54

    def display(self):
        print("The given distance in metres and cms is: {:.5f}".format(self.mtrs), " metres and ", self.cms, " cms.")


obj = MTRDistance()
obj.getinput()
obj.display()
