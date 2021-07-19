#module to get different time details
import datetime

#module to get current time
def get_time():
    time = datetime.datetime.now()
    current_time = time.strftime("%H hours %M minutes %S seconds")
    return current_time

def get_hour():
    time = datetime.datetime.now()
    hour = time.strftime("%H")
    return hour

def get_date():
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    return date
    




