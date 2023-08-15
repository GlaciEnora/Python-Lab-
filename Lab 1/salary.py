base = int(input("Enter the base salary of the employee: "))

ha = 0.3*base
ta = 0.15*base
pf = 0.05*base

print("Gross salary = %5.3f \nNet Salary = %5.3f"%(base+ha+ta, base+ta+ha-pf))
