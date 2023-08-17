#Lab-3 Ex1

def pkcharges(char, hour):
    if char == 'c':
        rate = 10

    elif char == 'b':
        rate = 20

    elif char == 't':
        rate = 5

    else:
        print("Not a valid parameter")
        return

    return rate*hour

typ = input("Enter the type of vehicle: ")
hr = int(input("Enter the number of hours clocked: "))
print("Parking charges for said vehicle: ", pkcharges(typ, hr))
