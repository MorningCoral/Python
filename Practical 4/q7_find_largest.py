# Finding the largest number in an array

alist = [5, 1, 8, 7, 2]

def find_largest(alist):
    if len(alist) == 1:
        return alist[0]

    else:
        m = find_largest(alist[1:])
        return m if m > alist[0] else alist[0]

print(find_largest(alist))
