# Computing GCD

def gcd (m,n):
    d = min(m,n)
    while (m % d == 0 and n % d == 0) is False:
        d -= 1
    print (d) 

gcd(24, 16)
gcd(225, 25)
