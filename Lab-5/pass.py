def check(arg):
    Ualnum, Lalnum, dignum, spcnum = 0, 0, 0, 0
    cons = ""
    for i in arg:
        if i.isalpha():
            cons += "1"
            if i.islower():
                Lalnum += 1
            else:
                Ualnum += 1
        elif i.isdigit():
            dignum += 1
            cons += "0"
        elif not(i.isalpha() and i.isdigit()) and i.isascii():
            cons += "1"
            spcnum += 1
    if 20 >= len(arg) >= 8:
        if Ualnum >= 1 and Lalnum >= 1 and dignum == 2 and spcnum == 1 and ("00" not in cons):
            print("The given string is a valid password...")
        else:
            print("The given string is not a valid password... ")
    else:
        print("The given string is not a valid password... ")

passw = input("Enter the string to validate as password: ")
check(passw)
