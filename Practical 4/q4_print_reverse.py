# Reverse the digits in an integer recursively

def reverse_int(n):
    s = str(n)
    if len(s) == 1:
        return n
    else:
        return reverse_int(s[1:]) + s[0]

print (reverse_int(1234))
