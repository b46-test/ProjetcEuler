from euler import is_palindrome

nombres={}

def retourne(nombre):
    total=0
    while nombre>0:
        total=total*10+nombre%10
        nombre=nombre/10
    return total
    
    
limite=500
    
for i in range(10000,1,-1):
    candidat=i+retourne(i)
    iterations=1
    while (not is_palindrome(candidat)) and iterations<limite:
        iterations+=1
        candidat+=retourne(candidat)
    
    if iterations==limite:
        print i,"est lychrel"
    else:
        print candidat,"est palindrome et vient de ",i,"apres iterations ",iterations
