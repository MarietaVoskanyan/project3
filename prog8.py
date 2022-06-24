def sum_of_days(year, month):
     
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        return 31
    elif month == 4 or 6 or 9 or 11:
        return 30
    elif month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
            
year1 = input("Input year: ")
month1 = input("Input month: ")
print (f'The sum of the days is: {sum_of_days(year1, month1)}')
sd
