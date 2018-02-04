# Computing the greatest common divisor


def gcd (n1,n2):
    d = min(n1,n2)
    while n1 % d != 0 or n2 % d != 0:
        d -= 1
    print (d) 

