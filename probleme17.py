#!/bin/env python

from numarray import *

unites=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
dizaines=["","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

total=0

for i in range(1,1001):
	texte=""
	print i
	if i==1000:	
		texte="onethousand"
	else:
		if i>99:
			texte=unites[i/100-1]+"hundred"	
			if i%100:
				texte+="and"
		
		d=i%100
		if d==0:
			texte+=""
		elif d<20:
			texte+=unites[d-1]
		else:
			texte+=dizaines[d/10-1]
			if d%10:
				texte+=unites[d%10-1]
	print texte
	print len(texte)
	total+=len(texte)
print total
