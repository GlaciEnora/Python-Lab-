def create_sentence(*lis):
    for text2 in lis[2]:
        for text1 in lis[1]:
            for text0 in lis[0]:
                print(" ".join(list((text0, text1, text2))))

lis1 = []
lis2 = []
lis3 = []
n = int(input("Enter the number of strings in each list: "))

for i in range(n):
    lis1.append(input("Enter element for list 1: "))
    lis2.append(input("Enter element for list 2: "))
    lis3.append(input("Enter element for list 3: "))

create_sentence(lis1, lis2, lis3)
