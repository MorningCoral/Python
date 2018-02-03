# Conversion from miles to kilometres

print("Miles\tKilometers\tKilometers\tMiles")

for i in range(10):
    mile1 = i +1
    km1 = mile1 *1.609
    km2 = 20 +(i*5)
    mile2 = km2* 0.6215
    print ("{0}\t{1:.3f}\t\t{2}\t\t{3:.3f}".format(mile1,km1,km2,mile2))
