# Finding the factors of an integer

def factor(n):
    i = 2
    factors = []
    
    def check(n):
        while n % i == 0:
            factors.append(str(i))
            n /= i
            
    while i <= n:
        check(n)
        while n % i == 0:
            n /= i
        i += 1
        
    print (','.join(factors))

factor(120)
    
