#Lab 2 Ex5

marks = []
tot = 0

for i in range(5):
    print("Enter the marks for the subject: ")
    mark = int(input())
    marks.append(marks)
    tot += mark

per = tot/5

print(per, "%")
if per >= 90:
    print("Grade A")

elif per >=80 and per <90:
    print("Grade B")

elif per >= 70 and per <80:
    print("Grade C")

elif per >= 60 and per <70:
    print("Grade D")

elif per >=40 and per <60:
    print("Grade E")

else:
    print("Grade F")
