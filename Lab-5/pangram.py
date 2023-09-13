def isPangram(arg):
    temp = ""
    for char in arg.lower().replace(" ", ""):
        if char not in temp:
            temp += char
    print(sorted(list(temp)))
    if len(temp) == 26:
        print("The given string is a pangram...")
    else:
        print("The given string is not a pangram")


isPangram(input("Enter the string to analyse: "))
        
