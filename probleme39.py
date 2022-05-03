from math import sqrt

maximum=0

for i in range(3,1001):
    total=0
    for a in range(1,i):
        for b in range(a,i):
            if a*a+b*b==(i-a-b)**2:
                print a,b,i-a-b
                total=total+1
    print i,total
    if total>maximum:
        gagnant=i
        maximum=total
