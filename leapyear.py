def leapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

# testcase1=leapYear(2015)
# print(testcase1)   
print(leapYear(2015))
print(leapYear(1970))
print(leapYear(1996))
print(leapYear(1960))
print(leapYear(2100))
print(leapYear(1900))
print(leapYear(2000))
print(leapYear(2400))
print(leapYear(1800))



    
     