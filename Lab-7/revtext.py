def revtext(name):
    file = open(name, 'r')
    for each in file:
        for item in each.split(" "):
            if item[0].lower() == 'i':
                print(item[::-1], end = " ")
            else:
                print(item, end = " ")

name = input("Enter the file to check: ")
revtext(name)
