# Checking whether a number is even
try:
    num = int(input("Enter number: "))
    if num % 2 == 0:
        print (str(num) + " is even")
    else:
        print ("%s is odd" %(num))
except ValueError:
    print("Please enter an integer")
