# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

nombre=600851475143239

# retourne -1 si le nombre est premier
# et le plus petit facteur premier sinon
def facteur(compose):
    i=2
    while i*i<compose:
        if compose%i==0 :
            return i
        i=i+1
    return -1


max=0

while facteur(nombre) != -1:
    nombre=nombre/facteur(nombre)
    
print nombre