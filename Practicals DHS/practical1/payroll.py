# payroll

name = input("Enter name: ")
hours = int(input("Enter number of hours worked weekly: "))
pay = float(input("Enter hourly pay rate: "))
cpfrate = float(input("Enter CPF contribution rate(%): "))
gross = pay * hours
cpf = gross * (cpfrate / 100)
netpay = gross - cpf

print (" ")
print ("Payroll statement for {0}".format(name))
print ("Number of hours worked in week: {0}".format(hours))
print ("Hourly pay rate: ${0:.2f}".format(pay))
print ("Gross pay: ${0:.2f}".format(gross))
print ("CPF contribution at {0}%: ${1:.2f}".format(cpfrate, cpf))
print ("Net pay: ${0:.2f}".format(netpay))
