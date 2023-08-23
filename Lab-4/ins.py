n = int(input("Enter the number of elements: "))
lis=[]
print("Enter the elements in sorted order")

while(n):
    lis.append(int(input("Enter element: ")))
    n-=1

x = int(input("Enter an element to insert: "))
for i in range(len(lis)):
    if lis[i] < x and i!=len(lis)-1:
        #print(i)
        pass
    elif lis[i] > x or i == len(lis)-1:
        if (lis[i] > x):
            lis.insert(i, x)
        else:
            lis.insert(i+1, x)
        break
    elif lis[i] == x:
        print("Duplicate element!")

print(lis)
