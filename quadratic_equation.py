import math
a,b,c = map(float,input("Enter a b c: ").split())
d = b*b - 4*a*c
if d >= 0:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print(r1, r2)
else:
    print("Complex roots")