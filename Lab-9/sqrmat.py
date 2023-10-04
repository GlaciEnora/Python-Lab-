class InvalidMatrix(Exception):
    pass
    
class sqr_matrix:
    row = 3
    col = 3

    def __init__(self):
        self.mat = [[None for i in range(self.row)] for i in range(self.col)]

    def input(self):
        try: 
            self.row = int(input("Enter the number of rows: "))
            self.col = int(input("Enter the number of columns: "))
            if self.row != self.col or self.row == 0 or self.col == 0:
                raise InvalidMatrix()
        except:
            print("The given matrix is an invalid matrix")
            return
            
        for i in range(self.row):
            for j in range(self.col):
                self.mat[i][j] = int(input())

    def check(self):
        flag = 5
        for i in range(self.row):
            for j in range(self.col):
                if i!=j and self.mat[i][j] == self.mat[j][i]:
                    flag = 1
                elif i!=j and self.mat[i][j] == -self.mat[j][i] and self.mat[i][i] == 0:
                    flag = -1
                if self.mat[i][i] == 0:
                    flag = 0
                if self.mat[i][i] == 1 and self.mat[i][j] == 0:
                    flag = 2
        if flag == -1:
            print("Given matrix is a skew-symmetric matrix")
        elif flag == 0:
            print("Given matrix is a diagonal matrix")
        elif flag == 1:
            print("Given matrix is a symmetric matrix")
        elif flag == 2:
            print("Given matrix is an identity matrix")
        else:
            print("Given matrix is a random matrix")

    def display(self):
        print(self.mat)

obj = sqr_matrix()
obj.input()
obj.display()
obj.check()
                
                    
