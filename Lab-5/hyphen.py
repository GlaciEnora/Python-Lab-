def convert(arg):
        lis = arg.split("-")
        lis.sort()
        return "-".join(lis)


string = input("Enter the string seperated by hyphens: ")
print(convert(string))
