# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten 
# natural numbers and the square of the sum is 3025 385 = 2640.

# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.

top=100

somme=0
somme_carres=0

for i in range(1,top+1):
    somme=somme+i
    somme_carres=somme_carres+i*i
    
print somme*somme
print somme_carres
print somme*somme-somme_carres