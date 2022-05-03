from math import sqrt

def nombre_de_diviseurs(nombre):
    total=0
    for i in range(1,int(sqrt(nombre))):
        if not nombre%i:
            total+=1
    
    return total*2

i=0
nombre=0
while(nombre<500):
    i+=1
    nombre=nombre_de_diviseurs(i*(i+1)/2)
    print i*(i+1)/2,nombre