from euler import chiffres
from euler import nombre_de_chiffres
from euler import somme_des_chiffres

i=0
reussi=False

nombre=100000
resume=1
while not reussi:
    nombre+=1
    reussi=True
    if(nombre_de_chiffres(nombre*6)>nombre_de_chiffres(nombre*2)):
        nombre=10**(nombre_de_chiffres(nombre)+1)
    actuel=chiffres(nombre*2)
    #print "***",nombre
    
    if somme_des_chiffres(nombre*2)%3:
        reussi=False
    else:
        for i in range(3,7):
            chiffres_multiple=chiffres(i*nombre)
            #print chiffres_multiple
            if not chiffres_multiple==actuel:
                #if i>3:
                    #for j in range(i+1):
                        #print j*nombre
                reussi=False
                break
        #if not nombre%resume:
            #print nombre

print nombre