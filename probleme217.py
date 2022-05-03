def est_balance(n):
    chiffres=[]
    while n>0:
        chiffres.append(n%10)
        n/=10
    if sum(chiffres[0:len(chiffres)/2])==sum(chiffres[len(chiffres)/2+1:len(chiffres)]):
        print "Oui!"
    else:
        print "Non!"


est_balance(11111111)
est_balance(1227320)
est_balance(13722)