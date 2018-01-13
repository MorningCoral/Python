# Interpret ASCII code
import string

code = int(input("ASCII code: "))

if 0 <= code <= 127:
    letter = chr(code)
    print ("Character: {0}".format(letter))
else:
    print ("Invalid Number!")
