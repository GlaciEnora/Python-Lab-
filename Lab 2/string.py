n = int(input("Enter the number of strings: "))
strlist = []
newlist1 = []
newlist2 = []
newlist3 = []

for i in range(n):
    temp = input("Enter string: ")
    strlist.append(temp)

for i in range(n):
    temp = ''
    for t in strlist[i]:
        if ord(t) >= 65 and ord(t)<91:
            temp += chr(ord(t)+32)

        elif ord(t) >= 97 and ord(t)<123:
            temp += chr(ord(t)-32)
    newlist1.append(temp)       
    
for i in range(n):
    temp = ''
    for t in strlist[i]:
        if t in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            pass

        else:
            temp += t
    newlist2.append(temp)

for i in range(n):
    temp = ''
    for t in strlist[i]:
        if t not in temp:
            temp += t
    newlist3.append(temp)

for i in range(n-1):
    if strlist[i] == strlist[i+1]:
        print("Duplicate value!")
        
print(newlist1, newlist2, newlist3)    