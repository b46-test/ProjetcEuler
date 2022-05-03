dict={}

for a in range(2,101):
    for b in range(2,101):
        cle=a**b
        if not dict.has_key(cle):
            dict[cle]=True

print len(dict)