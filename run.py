import functions

a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = int(input("Enter the number to reverse: "))

print("GCD of %d and %d is: "%(a,b), functions.gcd(a,b))
print("Reversing of %d is: "%c, functions.ReversingANumber(c))
