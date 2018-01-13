# Calculate volume of cyclinder

import math
radius = int(input("Radius: "))
length = int(input("Length: "))
area = radius * radius * math.pi
volume = area * length

print ("Volume of cylinder is {0:.1f}".format(volume))
