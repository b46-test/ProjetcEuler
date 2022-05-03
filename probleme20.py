# trouver la somme des chiffres de 100!

def facto(n):
    if n==1:
        return 1
    else:
        return n*facto(n-1)

def somme_des_chiffres(n):
    total=0
    while n>0:
        total=total+n%10
        n=n/10
        
    return total

print somme_des_chiffres(facto(100))
