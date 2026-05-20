a,b,c = map(int,input().split())
s = a+b+c
print(s*3 if a==b==c else s)