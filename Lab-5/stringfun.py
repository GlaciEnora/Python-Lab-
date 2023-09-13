def str_func(arg):
    if len(arg) < 2:
        print("Insufficient length to process...")
    elif len(arg) == 2:
        print(arg + "ing")
    elif len(arg) == 3:
        print(arg[-1] + "ed")
    else:
        print(arg[:2] + arg[-2:])


string = input("Enter the string to modify: ")
str_func(string)
