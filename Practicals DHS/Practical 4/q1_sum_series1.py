# Summing series

def sum_series(i):
    
    if i == 1:
        return 1
    else:
        return 1/i + sum_series(i-1)

    
