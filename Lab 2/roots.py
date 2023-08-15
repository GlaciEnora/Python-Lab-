#Lab 2 Ex 1

print("Enter the coefficients of the quadratic equation ax^2 + bx + c")
a = int(input("Coefficient of x^2: "))
b = int(input("Coefficient of x: "))
c = int(input("Constant value : "))

det = b**2 - (4*a*c)

if det > 0:
    print("Roots of the equation are: %5.3f %5.3f" %((-b+(det**0.5))/2*a, (-b-(det**0.5))/2*a))

elif det == 0:
    print("Roots of the equation are equal: ", b/(2*a))

else:
    print("Roots are not real and exist in the complex plane")
