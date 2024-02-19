from datetime import datetime

def date_difference_in_seconds(date1, date2):
    date_format = '%Y-%m-%d %H:%M:%S'
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)
    difference = abs(datetime2 - datetime1).total_seconds()
    return difference

date1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

difference_seconds = date_difference_in_seconds(date1, date2)
print("Difference between the two dates in seconds:", difference_seconds)
