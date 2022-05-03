fichier=open("probleme18.txt")

tableau=[]

lignes=fichier.readlines()
for ligne in lignes:
    #print ligne.split()
    tableau.append(ligne.split())
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            tableau[i][j]=int(tableau[i][j])
            
for i in range(1,len(tableau)):
    ligne=tableau[-1-i]
    for j in range(0,len(ligne)):
        print tableau[-i][j],tableau[-i][j+1]
        print tableau[-i-1][j]
        tableau[-1-i][j]=tableau[-1-i][j]+max(tableau[-i][j],tableau[-i][j+1])
        print tableau[-1-i][j]

for i in tableau:
    print i