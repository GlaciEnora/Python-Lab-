def credit(lis, accno, dep):
    flag = False
    for item in lis:
        if accno in item:
            flag = True
            item[2] += dep
            print(item)
    if not flag:
        print("The given account no is not available in the records...")    
    
def debit(lis, accno, amt):
    flag = False
    for item in lis:
        if accno in item:
            flag = True
            if amt > item[2]:
                print("Not possible to debit...")
            else:
                item[2] -= amt
                print(item)
    if not flag:
        print("The given account no is not available in the records...")

def ordered(lis):
    l = len(lis)
     
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (lis[j][2] > lis[j + 1][2]):
                lis[j], lis[j+1] = lis[j+1], lis[j]
    print(lis)
