d = {}
n = int(input("Enter the number of customers: "))
for i in range(n):
    key = input("Enter customer name: ")
    val = {}
    val["AccNo"] = int(input("Enter the account number: "))
    val["Name"] = input("Enter the name: ")
    val["Balance"] = int(input("Enter balance: "))
    d[key] = val
lis = []
try:
    for dic in d.values():
        try:
            if dic["AccNo"] > 100: lis.append(dic)
            if dic["AccNo"] < 100:
                    raise NameError
        except NameError:
             print(dic)
finally:
     print(lis)

    
        
