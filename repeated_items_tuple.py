t = tuple(input().split())
for i in set(t):
    if t.count(i)>1:
        print(i)