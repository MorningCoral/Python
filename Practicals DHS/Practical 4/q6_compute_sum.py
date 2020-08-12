# Summing the digits in an integer using recursion

def sum_digits(n):
    s = str(n)
    if len(s) == 1:
        return n
    else:
        return int(s[0]) + sum_digits(int(s[1:]))
