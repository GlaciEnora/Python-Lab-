#Lab2 Ex7

n = int(input("Enter the number to find: "))
fac_str = ""
pri_str = ""

for i in range(2, n+1):
    if n%i == 0:
        fac_str += str(i)+" "
        for j in range(2, i+1):
            if (i%j == 0) and i != j:
                break
        else:
            pri_str += str(i) + " "
            

print("Factors of %d are: "%n, fac_str)
print("Prime factors of %d are: "%n, pri_str)
