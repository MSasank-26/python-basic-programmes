n=int(input())
row=[1]
for i in range(n):
    print(row)
    row=[sum(x) for x in zip([0]+row,row+[0])]