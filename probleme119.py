def digits(n):
    somme=0
    while n>=10:
        somme+=n%10
        n=n/10
    return somme+n
    
nombre=0
longmax=300
i=11
liste=[]
for i in range(2,longmax*9):
    for n in range(2,50):
        if digits(i**n)==i:
            print i**n,i,n
            liste.append(i**n)
            
liste.sort()
for i in liste:
    print i
print liste[1]
print liste[9]
print liste[44]