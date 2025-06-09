def is_year_leap(year):
#
# Write your code here.
#
    leap_year = 44
    leap_years = [""]
   # leap_years.append["1904"]
    for i in range(1,1001):
      leap_year += 4
      leap_years.append(leap_year)
    print(leap_years)
    for b in leap_years:
        if b == year:
            return True
    
    return False
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

myyear = int(input("enter year: "))
result2 = is_year_leap(myyear)
if result2 == True:
    print("Leap")
else:
    print("No Leap")
