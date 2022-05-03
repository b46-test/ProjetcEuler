from euler import somme_des_diviseurs


touches={}

total=0

for i in range(100000):
    
    somme=somme_des_diviseurs(i)
    petit=min(i,somme)
    grand=max(i,somme)
    
    if touches.has_key(petit):
        if touches[petit]==grand:
            print petit,grand
            total+=petit+grand
    else:
        touches[petit]=grand

print total