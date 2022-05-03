from numpy import ones
from numpy import zeros

c=0
p=0
rounds=0

resume=1000



des_p=ones(6)

des_c=ones(9)

somme=0
nombres_p=zeros(37)
nombres_p[6]=1
while somme<36:
    i=0
    while des_p[i]==6:
        des_p[i]=1
        i+=1
        
    des_p[i]+=1
    
    somme=sum(des_p)
    
    #print des_p
    
    nombres_p[somme]+=1
    
somme=0
nombres_c=zeros(37)
nombres_c[9]=1
while somme<36:
    
    i=0
    while des_c[i]==4:
        des_c[i]=1
        i+=1
        
    des_c[i]+=1
    
    somme=sum(des_c)
    
    #print des_c
    
    nombres_c[somme]+=1
    
print nombres_p
print nombres_c

print sum(nombres_p),6**6
print sum(nombres_c),4**9

gagnants=0
for i in range(9,37):
    print i,nombres_c[i]
    gagnants+=nombres_c[i]*sum(nombres_p[0:i])
    
print float(gagnants)/(6**6*4**9)
