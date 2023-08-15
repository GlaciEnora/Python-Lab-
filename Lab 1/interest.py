pri = int(input("Enter the principle amount: "))
rate = int(input("Enter the rate of interest as percentage: "))
year = int(input("Enter the amount of years: "))

print("Simple interest = ", pri*rate*year/100)
print("Amount acquired through compound interest = ", pri*(1+(rate/(100*year) \
                                                              ))**year)
