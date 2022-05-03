#1_2_3_4_5_6_7_8_9
#101010101
#138902662
for i in range(101010101,138902662):
    texte=str(i**2)
    #print texte
    reussi=True
    #print len(texte)
    for j in range(9):
        #print texte[2*j],j+1
        if not texte[2*j]==str(j+1):
            reussi=False
            break
    if reussi:
        print "***",i
            
    if not i%(10**6):
        print i
