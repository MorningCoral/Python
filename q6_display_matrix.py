# Displaying matrix of 0s and 1s
import random

def print_matrix(n):
    matrix = []
    for i in range(0,n*n):
        x = random.randint(0,1)
        matrix.append(str(x))
        
    for i in range(0,n*n,n):
        print(" ".join(matrix[i:i+n]))

print_matrix(5)
