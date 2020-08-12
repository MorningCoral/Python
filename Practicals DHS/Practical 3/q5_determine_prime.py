# Prime number

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
                break
        return True
    
prime = []
i = 2
while len(prime) < 1000:
    if is_prime(i) == True:
        prime.append(str(i))
    i += 1

for t in range(0,1000,10):
    print("\t".join(prime[t:t+10]))
