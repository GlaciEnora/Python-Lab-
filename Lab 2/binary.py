#Lab2 Ex9 KILL ME ALREADY

list_num = []

n = int(input("Enter the number of terms: "))
k = n
while k !=0:
    num = int(input("Enter the number: "))
    list_num.append(num)
    k -= 1
print(list_num)

for i in range(n):
    for j in range(0, n-i-1):
        if list_num[j] > list_num[j+1]:
            list_num[j], list_num[j+1] = list_num[j+1], list_num[j]

print(list_num)
tar = int(input("Enter the target to search: "))

low, high = 0, len(list_num)

while low < high:
    mid = low+high/2
    print("Entering loop")
    if mid < tar:
        low = mid + 1
        print("Low increment")

    elif mid > tar:
        high = mid - 1
        print("High decrement")

    elif mid == tar:
        print("Element found at position %d"%mid)
        break

if low > high:
    print("Element not found")



            
