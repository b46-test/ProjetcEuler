# A Pythagorean triplet is a set of three natural numbers, a  b  c, for 
# which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for i in range(1,998):
    for j in range(i,998-i):
        k=1000-i-j
        if i*i+j*j==k*k:
            print i,j,k
            print i*j*k