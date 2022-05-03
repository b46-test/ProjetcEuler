longueur=10
total=0

def perm(nombre):
    global total
    if len(nombre)<longueur:
        for i in range(longueur):
            if not str(i) in nombre:
                perm(nombre+str(i))
    else:
        total=total+1
        print total,":",nombre
    
    return
    
perm("")