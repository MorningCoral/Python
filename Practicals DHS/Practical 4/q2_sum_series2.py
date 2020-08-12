# Summing series

def sum_series(i):
    
    if i == 1:
        return 1/3
    else:
        return i/(2*i+1) + sum_series(i-1)

    
print(sum_series(3))
