from math import sqrt
def solutions(n):
    if n%4:
        return 0
    
    total=0
    i=1
    #print "***",
    while 4*i*i<n:
        bords=n/4-i*i
        #print bords
        if not (bords)%i:
            total+=1
            #print i*i,bords/i,i*i*4+bords*4
            #print "Oui"
        i+=1
    return total

compte=0
resume=100000
#print solutions(0)
#print solutions(32)
for i in range(8,1000004,4):
    nombre=solutions(i)
    if not i%resume:
        print i,nombre,compte
    #if nombre<=10:
    compte+=nombre
print compte