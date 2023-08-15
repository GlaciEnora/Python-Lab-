#Lab 2 Ex2

print("Enter the three numbers: ")
a = int(input())
b = int(input())
c = int(input())

print(a, "is the greatest") if(a > b and a > c) else \
         print(b, "is the greatest") if(b > a and b >c) else print(c, "is the greatest")
