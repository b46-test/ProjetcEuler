
# It can be verified that T_(285) = P_(165) = H_(143) = 40755.

# Find the next triangle number that is also pentagonal and hexagonal.

def pentagonal(candidat):
    return candidat*(3*candidat-1)/2

def hexagonal(candidat):
    return candidat*(2*candidat-1)




touches={}


# les nombres hexa sont aussi triangulaires. Il 
# suffit de tester les deux dernières conditions
for i in range(100000):
    pent=pentagonal(i)
    touches[pent]=1

for i in range(100000):
    hexa=hexagonal(i)
    if touches.has_key(hexa):
        touches[hexa]+=1
        print hexa, touches[hexa]