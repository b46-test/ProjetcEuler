l=50

nb=0

for x1 in range(l+1):
	for y1 in range(l+1):
		for x2 in range(x1,l+1):
			if(x2==x1):
				w=y1
			else:
				w=0
			for y2 in range(w,l+1):
				if (x1,y1)==(x2,y2) or (x1,y1)==(0,0):
					pass
				else:
					if(x1*x2+y1*y2==0) or (x1*(x2-x1)+y1*(y2-y1)==0) or (x2*(x1-x2)+y2*(y1-y2)==0):
						nb+=1
						print x1,y1,x2,y2
print nb
