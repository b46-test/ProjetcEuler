compte=0
for i in range(1,25):
    for j in range(1,10):
        if(len(str(j**i))==i):
            print j,i
            compte+=1
print compte