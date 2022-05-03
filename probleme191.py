def prix(s):
    if(s.count("L"))>1:
        return False
    if(s[-5:].find("AAA")!=-1):
        return False
    else:
        return True

cache={}
nombre_de_jours=30
def compte(s):
    #print s
    #if(not prix(s)):
        #return 0
    if(len(s)==nombre_de_jours):
        return 1
    else:
        retard=s.count("L")
        if s[-2:]=="LA":
            absences="OA"
        else:
            absences=s[-2:]
        cle=str(retard)+absences+str(len(s))
        if cache.has_key(cle):
            return cache[cle]
        total=0
        if not retard:
            total+=compte(s+"L")
        
        if not s[-2:]=="AA":
            total+=compte(s+"A")
        
        total+=compte(s+"O")
        
        cache[cle]=total
        
        return total


print compte("")
