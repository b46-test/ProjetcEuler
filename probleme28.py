pas=2
angle=1
somme=1

for i in range(500):
	for j in range(4):
		angle+=pas
		somme+=angle
		print angle
	print
	pas+=2
print somme
