from euler import premiers

limite=50000000

liste=premiers(limite**2*2)


i=1
nombre=0

while nombre<limite:
    i+=1
    nombre=2*i*i-1
    if liste[i]:
        total+=1
        
print total