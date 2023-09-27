import csv

with open("student.csv", mode='r') as file:
    csvreader = csv.reader(file)

    for line in csvreader:
        if (line[0] != 'RollNo'):
            s = 0
            for i in line[2:]:
                s += int(i)
            if s > 250:
                print(line)
        elif line[0] == 'RollNo':
            print(line)



