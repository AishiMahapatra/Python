number_of_years = int(input('Enter the number of years' ))
sum_of_rainfall_in_inches = 0
for x in range(number_of_years):
 for y in range(12):
     inches_of_rainfall = int(input('Enter the inches of rainfall in month'))
     sum_of_rainfall_in_inches = sum_of_rainfall_in_inches + inches_of_rainfall
print('Average rainfall in this period is',sum_of_rainfall_in_inches/(number_of_years*12))
