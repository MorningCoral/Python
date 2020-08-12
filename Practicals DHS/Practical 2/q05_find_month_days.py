# Finding the number of days in a month

try:
    month = int(input("Enter month: "))
    year = int(input("Enter year: "))

    if month == 1:
        print("January %s has 31 days" %(year))
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print("February %s has 29 days" %(year))
        else:
            print("February %s has 28 days" %(year))
    elif month == 3:
        print("March %s has 31 days" %(year))
    elif month == 4:
        print("April %s has 30 days" %(year))
    elif month == 5:
        print("May %s has 31 days" %(year))
    elif month == 6:
        print("June %s has 30 days" %(year))
    elif month == 7:
        print("July %s has 31 days" %(year))
    elif month == 8:
        print("August %s has 31 days" %(year))
    elif month == 9:
        print("September %s has 30 days" %(year))
    elif month == 10:
        print("October %s has 31 days" %(year))
    elif month == 11:
        print("November %s has 30 days" %(year))
    elif month == 12:
        print("December %s has 31 days" %(year))
    else:
        print("Invalid month!")
except ValueError:
    print("Please enter a valid number")
    
