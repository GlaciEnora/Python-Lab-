sname = []
roll = []
cgpa = []
n = int(input("Enter the number of students: "))
for i in range(n):
        sname.append(input("Enter the student name: "))
        roll.append(int(input("Enter the roll number: ")))
        cgpa.append(float(input("Enter the current cgpa: ")))

for i in range(n):
        print("Student name: ", sname[i])
        print("Roll number: ", roll[i])
        print("CGPA = ", cgpa[i])
