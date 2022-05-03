def voyage(n):
    if n==2:
        print 2,"->",1,"[pos=\"20,100\"]"
        return
    elif n%2:
        print n,"->",3*n+1,"[pos=\"",20*n,",100\"]"
        voyage(3*n+1)
        return
    else:
        print n,"->",n/2,"[pos=\"",20*n,",100\"]"
        voyage(n/2)
        return

for i in range(1,100):
    voyage(i)