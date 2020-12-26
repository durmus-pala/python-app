year = input("Please enter a 4 digit year: ")
is_leap_year = True
if (int(year) % 4 == 0) and (int(year) % 100 != 0):
  is_leap_year = True
elif (int(year) % 4 == 0) and (int(year) % 400 == 0):
  is_leap_year = True
else:
  is_leap_year = False
print("The leap year condition of the year which you enter is:", is_leap_year)
