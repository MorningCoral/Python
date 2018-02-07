# Summing series

def m_series(i):
    print("i\tm(i)")
    
    for n in range(1, i+1):
        sum = 0
        for x in range(n+1):
            sum += x / (x+1)
        print ("{0}\t{1:.4f}".format(n,sum))
        
m_series(20)
