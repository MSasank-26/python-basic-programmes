amount = int(input())
notes = [500,200,100,50,20,10,5,2,1]
for i in notes:
    print(i, ":", amount//i)
    amount %= i