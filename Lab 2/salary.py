#Lab 2 Ex4

base = int(input("Enter the base salary of the employee: "))

if base <= 10000:
    hra = 0.2 * base
    da = 0.8 * base
    print("Gross salary: ", base + hra + da)

elif base > 10000 and base <= 20000:
    hra = 0.25 * base
    da = 0.9 * base
    print("Gross salary: ", base + hra + da)

else:
    hra = 0.3 * base
    da = 0.95 * base
    print("Gross salary: ", base + hra + da)

    
