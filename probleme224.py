# coding=UTF-8

from math import sqrt
limite=100000

a=0
nombre=0

resume=1000

while a<limite-2:
    a+=1
    b=a
    while a+b+sqrt(a*a+b*b+1)<=limite:
        truc=sqrt(a*a+b*b-1)
        if truc==int(truc):
            #print a,b,truc,a*a,b*b,truc*truc
            nombre+=1
        b=b+1
        
    if not a%resume:
        print a,b,truc,a*a,b*b,truc*truc
        
print nombre