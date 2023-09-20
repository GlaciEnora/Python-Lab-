def long(name):
    file = open(name, 'r')
    maxi = ""
    for each in file:
        for item in each.split(' '):
            if len(maxi) < len(item):
                maxi = item
    return maxi


name = input("Enter the name of the file: ")
print("The longest word is : ", long(name))
        
