def somme_des_chiffres(n):
    total=0
    while n>0:
        total=total+n%10
        n=n/10
        
    return total
    
print 2**10
print somme_des_chiffres(2**1000)