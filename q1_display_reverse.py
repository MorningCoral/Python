# Displaying an integer reversed

def reverse_int(n):
    reverse = []
    num = str(n)
    for i in num:
        reverse.insert(0,i)
    print (''.join(reverse))

reverse_int(3456)
    
