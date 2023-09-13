from datetime import datetime

def email(lis):
    mail = []
    mail.append(lis[0] + "@sastra.ac.in")
    return mail

def create(n, lis):
    for i in range(n):
        newlist = []
        newlist.append(input("Enter the reg no: "))
        newlist.append(input("Enter the name: "))
        dob = datetime.strptime(input("Enter dob: "), "%d/%m/%Y")
        #newlist.append(dob)
        newlist.append(dob.strftime("%d/%m/%Y"))
        age = datetime.today().year - dob.year
        newlist.append(age)
        newlist.append(email(newlist))
        lis.append(newlist)

def displaycheck(lis):
    template = "{:<10}{:<15}{:>14}{:>05}{:<25}{:^30}"
    print(template.format("Reg No", "Name", "Date of Birth", "Age", "Email id", "Eligibility for voting"))
    for item in lis:
        if item[3] >= 18:
            choice = "yes"
        else:
            choice = "no"
        print(template.format(item[0], item[1], item[2], item[3], item[4], choice))
        
new = []
create(1, new)
print(new)
displaycheck(new)
        
