#Years that are exactly divisible by four are a leap year.
#Years that are exactly divisible by 100 are not a leap year.
#Years that are exactly divisible by 400 are a leap year.

year = int(input("What year is it? "))

if (year % 100 == 0 and year % 400 == 0):
    print("Year {} is a leap year".format(year))
elif (year % 4 == 0 and year % 100 != 0):
    print("Year {} is a leap year".format(year))
else:
    print("Year {} is not a leap year".format(year))