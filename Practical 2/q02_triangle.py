# Validating triangles and computing perimeter

a = int(input("Enter side: "))
b = int(input("Enter side: "))
c = int(input("Enter side: "))

if (a+b) > c and (a+c) > b and (b+c) > a:
    p = a+b+c
    print("Perimeter = " + str(p))
else:
    print("Invalid triangle!")
