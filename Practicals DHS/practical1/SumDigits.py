# Summing the digits in an integer

num = int(input("Integer between 0 and 1000: "))
if 0 < num < 1000:
    ones = num % 10
    tens = (num // 10) % 10
    hundreds = (num // 100)
    sum = ones + tens + hundreds
    print ("Sum of digits: {0}".format(sum))
else:
    print ("Invalid Number!")

