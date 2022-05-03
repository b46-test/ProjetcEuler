#28433x2^(7830457)

def puissance_imprecise(a,b,precision):
    resultat=1
    while b>0:
        if b%2:
            resultat=(resultat*a)%10**precision
        a=a*a
        b/=2
    return resultat
        
print (28433*puissance_imprecise(2,7830457,10)+1)%10**10