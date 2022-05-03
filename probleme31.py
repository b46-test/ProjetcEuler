valeurs=[200,100,50,20,10,5,2,1]


total=0

for i in range(2):
    for j in range(3):
        if i*200+j*100>200:
            break
        for k in range(5):
            if k*50+i*200+j*100>200:
                break
            print i,j,k
            for l in range(11):
                if l*20+k*50+i*200+j*100>200:
                    break
                for m in range(21):
                    if m*10+l*20+k*50+i*200+j*100>200:
                        break
                    for n in range(41):
                        if n*5+m*10+l*20+k*50+i*200+j*100>200:
                            break
                        for o in range(101):
                            if o*2+n*5+m*10+l*20+k*50+i*200+j*100>200:
                                break
                            total+=1
print total