from itertools import chain,combinations

tentative=[11,17,20,22,23,24,300]

def powerset(iterable):
  xs = list(iterable)
  # note we return an iterator rather than a list
  return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )


def is_special(liste):
	a=[sum(x) for x in powerset(liste)]
	if len(a)==len(set(a)) and sum(liste[:(len(liste)+1)/2])>sum(liste[-len(liste)/2+1:]):
		return True
	return False

print is_special(tentative)
print is_special([11, 18, 19, 20, 22, 25])
print is_special([20,31,38,39,40,42,45])
tentative=[20,31,38,39,40,42,45]

assert(is_special(tentative))
for a in range(1,tentative[-1]):
	for b in range(a+1,tentative[-1]):
		for c in range(b+1,tentative[-1]):
			if is_special([a,b,c]) and sum([a,b,c])>=9 and sum([a,b,c])<sum(tentative)-4*c:
				for d in range(c+1,tentative[-1]):
					if is_special([a,b,c,d]) and sum([a,b,c,d])>=21 and sum([a,b,c])<sum(tentative)-3*d:
						for e in range(d+1,tentative[-1]):
							print a,b,c,d,e
							if is_special([a,b,c,d,e]) and sum([a,b,c,d,e])<sum(tentative) and sum([a,b,c,d,e])>=51:
								for f in range(e+1,tentative[-1]):
									for g in range(f+1,sum(tentative)-sum([a,b,c,d,e,f])):
										if is_special([a,b,c,d,e,f,g]):
											print a,b,c,d,e,f,g
											if sum([a,b,c,d,e,f,g])<sum(tentative):
												tentative=[a,b,c,d,e,f,g]
						
print tentative
