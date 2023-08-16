def net_sal(base, HRA, TA, PF):
    net = base+HRA+TA-PF
    return net

def calculation(baselist):
    netlist = []
    for i in range(len(baselist)):
        HRA = baselist[i]*0.10
        TA = baselist[i]*0.05
        PF = baselist[i]*0.04
        netlist.append(net_sal(baselist[i], HRA, TA, PF))
    return netlist

n = int(input("Enter the number of employees: "))
baselist = []
print("Enter the employee salaries: ")
for i in range(0, n):
    baselist.append(int(input()))
print("Net salary of employees: ", calculation(baselist))
