def puissance_imprecise(base,exposant,precision):
    return (base**exposant)%(10**precision)


def somme_imprecise(a,b,precision):
    return (a+b)%(10**precision)

total=0
for i in range(1,1000):
    total=somme_imprecise(total,puissance_imprecise(i,i,10),10)
    
print total
