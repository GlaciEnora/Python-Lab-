import interest

pri = int(input("Enter principle: "))
rate = float(input("Enter rate: "))
time = int(input("Enter the time in months: "))

print(interest.simp_intr(pri, time))
print(interest.simp_intr(pri, time, rate))
print(interest.comp_intr(pri, time, rate))
