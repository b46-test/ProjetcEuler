from euler import nombre_de_chiffres


ancien=1
actuel=1
n=2
while nombre_de_chiffres(actuel)<1000:
    n,ancien,actuel=n+1,actuel,ancien+actuel
    print n#,actuel