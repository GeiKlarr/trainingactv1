from datetime import datetime

def calDate(dateA,dateB):

    date1 = datetime.strptime(dateA,"%m-%d-%Y")
    date2 = datetime.strptime(dateB, "%m-%d-%Y")
    #datetime.strptime(date_string, format)

    result = date1 - date2

    return result.days

dateA = "1-1-2023"
dateB = "2-2-2023"

daysDiff = calDate(dateA,dateB)

print("Number of days between the dates:",abs(daysDiff))