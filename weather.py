import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celsius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celsius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    dt=datetime.fromisoformat(iso_string)
    return f"{dt.strftime('%A')} {dt.strftime('%d')} {dt.strftime('%B')} {dt.year}"


def convert_f_to_c(temp_in_fahrenheit):
    """Converts an temperature from fahrenheit to celsius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celsius, rounded to 1dp.
    """
    num=float(temp_in_fahrenheit)
    a= -17.77777777777778
    b=17.77777777777778 / 32 *(num)
    return round(a + b,1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    list = [float(x) for x in weather_data]
    return sum( number for number in list)/len(weather_data)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list = []
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if len(line)> 0:
                list.append(line)
    list.pop(0)
    for x in list:
        x[1]=int(x[1])
        x[2]=int(x[2])
    return list
#print(list)




def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if  weather_data == []:
        return ()
    else:
        min_val = weather_data[0]
        min_position = 0
        index = 0
        for x in weather_data:
            if x <= min_val:
                min_val = x
                min_position = index
            index +=1
        #min_position = max( index for index, x in enumerate(weather_data) if x == min_val)
    return (float(min_val), min_position)
            


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if  weather_data == []:
        return ()
    else:
        max_val = weather_data[0]
        max_position = 0
        index = 0
        for x in weather_data:
            if x > max_val:
                max_val = x
                max_position = index
            index +=1
        max_position = max( index for index, x in enumerate(weather_data) if x == max_val)
    return (float(max_val), max_position)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    days = len(weather_data)

    temp_min = [x[1] for x in weather_data]
    temp_max = [y[2] for y in weather_data]

    list_date = [d[0] for d in weather_data]
    #print(list_date)
    lowest_tem = format_temperature(convert_f_to_c(find_min(temp_min)[0]))
    date_min = convert_date(list_date[find_min(temp_min)[1]])
    highest_tem = format_temperature(convert_f_to_c(find_max(temp_max)[0]))
    date_max = convert_date(list_date[find_max(temp_max)[1]])
    min_av = format_temperature(convert_f_to_c(calculate_mean(temp_min)))
    max_av = format_temperature(convert_f_to_c(calculate_mean(temp_max)))
    return f"{days} Day Overview\n  The lowest temperature will be {lowest_tem}, and will occur on {date_min}.\n  The highest temperature will be {highest_tem}, and will occur on {date_max}.\n  The average low this week is {min_av}.\n  The average high this week is {max_av}.\n"
    

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    day_m = ""
    for line in weather_data:
        day_m = day_m + f"---- {convert_date(line[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(line[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(line[2]))}\n\n"
    return day_m

