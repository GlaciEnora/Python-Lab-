class distance:
    d = {'':{}}

    def __init__(self):
        del self.d['']
        for i in range(5):
            self.d['Dist'+str(i+1)] = {}

    def input(self):
        for i in self.d.keys():
            self.d[i]['Feet']=float(input("Enter the feet: "))
            self.d[i]['Inches']=float(input("Enter the inches: "))

            if self.d[i]['Inches'] > 12:
                self.d[i]['Inches'] -= 12
                self.d[i]['Feet'] += 1
            
    def display(self):
        print(self.d)
        for i in self.d.keys():
            print(i, self.d[i])

class Operation:
    result_feet = 0
    result_inches = 0

    def __init__(self):
        self.dist = distance()
        self.dist.input()

    def average(self):
        for i in self.dist.d.keys():
            self.result_feet += self.dist.d[i]['Feet']
            self.result_inches += self.dist.d[i]['Inches']
        self.result_feet /= 5
        self.result_inches /= 5
        if self.result_inches > 12:
            self.result_inches -= 12
            self.fesult_feet += 1
        print("Average of all distances is: ", self.result_feet, " feet and ", self.result_inches, " inches.")

    def add_distance(self):
        self.result_feet = self.dist.d['Dist1']['Feet'] + self.dist.d['Dist2']['Feet']
        self.result_inches = self.dist.d['Dist1']['Inches'] + self.dist.d['Dist2']['Inches']
        if self.result_inches > 12:
            self.result_inches -= 12
            self.result_feet += 1
        print("Addition of two distances is: ", self.result_feet, self.result_inches)

    def maximum(self):
        arg = []
        maxf = 0
        maxi = 0
        for i in self.dist.d.keys():
            arg.append([self.dist.d[i]['Feet'], self.dist.d[i]['Inches']])
        for item in arg:
            if maxf < item[0] and maxi < item[1]:
                maxf = item[0]
                maxi = item[1]
        print("Maximum distance is: ", maxf, " feet and ", maxi, " inches.")
        
    def display(self):
        print(self.dist.d)
        print(self.result_feet)
        print(self.result_inches)
            
obj = Operation()
obj.average()
obj.maximum()
obj.add_distance()
obj.display()
