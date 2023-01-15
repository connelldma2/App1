FILEPATH = "../MyFiles/Weather.csv"

import csv

with open(FILEPATH, 'r') as file:
    weather_data = list(csv.reader(file))

print(weather_data)
print(type(weather_data))

city_name = input("Enter city: ")

for row in weather_data[1:]:
    if row[0] == city_name:
        current_temp = row[1]
    else:
        current_temp = 'No Data'

if current_temp == 'No Data':
    print('No data available.')
else:
    print(f'Current Temperature: {current_temp} degrees Celsius')