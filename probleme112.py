def bouncy(n):
    estBouncy=False
    if n<100:
        return False
    while n%10==(n/10)%10:
        n=n/10
        
    if n%10<(n/10)%10:
        #print n
        while n>=10 and not estBouncy:
            #print n
            if n%10>(n/10)%10:
                estBouncy=True
            n=n/10
    else:
        #print "*",n
        while n>=10 and not estBouncy:
            #print "*",n
            if n%10<(n/10)%10:
                estBouncy=True
            n=n/10
    
    return estBouncy
        
    
        
bouncies=0
n=1
proportion=0
resume=1000000
#print bouncy(77227)
while n<100 or proportion<.99:
    n+=1
    resultat=bouncy(n)
    if resultat:
        bouncies+=1
    proportion=float(bouncies)/n
    if not n%resume:
        print n,resultat,proportion
print n