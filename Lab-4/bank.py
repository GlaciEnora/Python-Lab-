from transaction import *

bankdet = []

N = int(input("Enter the number of customers: "))
for i in range(N):
    inner = []
    inner.append(input("Enter customer name: "))
    inner.append(input("Enter the account number: "))
    inner.append(int(input("Enter the current holding balance: ")))
    bankdet.append(inner)
print(bankdet)
while True:
    choice = input("Enter the operation to perform: ")
    if choice.title() == "Credit":
        acc = input("Enter the account number: ")
        dep = int(input("Enter amount to credit: "))
        credit(bankdet, acc, dep)
    elif choice.title() == "Debit":
        acc = input("Enter the amount number: ")
        amt = int(input("Enter the amount to debit: "))
        debit(bankdet, acc, amt)
    elif choice.title() == "Order":
        ordered(bankdet)
    else:
        break