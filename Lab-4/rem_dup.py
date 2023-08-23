def rem_dup(arg):
     for i in range(len(arg)):
        if i == len(arg):
             break
        for j in range(len(arg)):
                if j == len(arg):
                     break
                if arg[i] == arg[j] and i != j:
                    arg.remove(arg[j])
        print(len(arg))
                
n = int(input("Enter the number of elements: "))
lis=[]
while(n):
    lis.append(int(input("Enter element: ")))
    n-=1

print(lis)
rem_dup(lis)
print(lis)
                

        


        
