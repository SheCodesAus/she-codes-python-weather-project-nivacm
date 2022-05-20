import csv
weather_data = []
with open('tests/data/example_one.csv') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if len(line)> 0:
                weather_data.append(line)
weather_data.pop(0)
print()
print(weather_data)
days = len(weather_data)
print(days)
print()
temp_min = [x[1] for x in weather_data]

print(temp_min)
temp_max = [y[2] for y in weather_data]
print(temp_max)
list_date = [x[0] for x in weather_data]

print(list_date)

# from datetime import datetime

# DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


# def format_temperature(temp):
#     """Takes a temperature and returns it in string format with the degrees
#         and celsius symbols.

#     Args:
#         temp: A string representing a temperature.
#     Returns:
#         A string contain the temperature and "degrees celsius."
#     """
#     return f"{temp}{DEGREE_SYBMOL}"


# def convert_date(iso_string):
#     """Converts and ISO formatted date into a human readable format.

#     Args:
#         iso_string: An ISO date string..
#     Returns:
#         A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
#     """
#     dt=datetime.fromisoformat(iso_string)
#     return f"{dt.strftime('%A')} {dt.strftime('%d')} {dt.strftime('%B')} {dt.year}"

# print(convert_date('2010-09-12'))
# def convert_f_to_c(temp_in_fahrenheit):
#     num = float(temp_in_fahrenheit)
#     a= -17.777
#     b=17.777 / 32 *float(num)
#     return round(a + b,1)
# print(convert_f_to_c(0))

# def calculate_mean(weather_data):
#     """Calculates the mean value from a list of numbers.

#     Args:
#         weather_data: a list of numbers.
#     Returns:
#         A float representing the mean value.
#     """
    
#     return float(sum(x for x in weather_data)/len(weather_data))

# print(calculate_mean([2,4,6,8]))
# print()
# import csv

# list_1 = []
# with open('tests/data/example_three.csv') as csv_file:
#         reader = csv.reader(csv_file)
#         for line in reader:
#             if len(line)> 0:
#                 list_1.append(line)
# list_1.pop(0)
# #print(list_1)
# for x in list_1:
#     x[1]=int(x[1])
#     x[2]=int(x[2])
# print(list_1)
# print()

# x=[]
# min(x)