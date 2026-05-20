n = int(input())
s = sum(int(i)**len(str(n)) for i in str(n))
print("Armstrong" if s==n else "Not Armstrong")