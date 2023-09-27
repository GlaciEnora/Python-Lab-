import csv

field = ['Prod ID', 'Prod Name', 'Price']
with open("prod.csv", 'w', newline='') as fin:
    csin = csv.DictWriter(fin, fieldnames=field)
    csin.writeheader()
    n = int(input("Enter the number of products: "))
    for i in range(n):
        dic = eval(input())
        csin.writerow(dic)

with open("prod.csv", 'r', newline='') as fout:
    csout = csv.DictReader(fout)
    pricelist=[]
    for row in csout:
        pricelist.append(int(row['Price']))
    fout.seek(len(','.join(field))+1)
    for row in csout:
        if (int(row["Price"]) == max(pricelist)):
            print(row)
