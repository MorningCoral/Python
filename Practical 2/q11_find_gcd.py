# Computing the greatest common divisor


def gcd (n1,n2):
    i = 1
    while n1 % i == 0 and n2 % i == 0:
        i += 1
    print (i - 1) 

gcd(5,9)
gcd(3,9)
gcd(48,24)
gcd(66,77)
