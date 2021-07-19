# how does assistant greets on
from date_time_module import get_hour, get_date
from output_module import output
import database


def greet_user():

    previous_date = database.get_last_seen()
    current_date = get_date()
    database.update_last_seen(current_date)
    
    if current_date == previous_date:
        output("Welcome back,need me again")
    else:    
        hour = int(get_hour())
        if hour>=4 and hour <12:
            output("Good Morning")
        
        elif hour>12 and hour<=16:
            output("Good Afternoon")

        elif hour>16 and hour<=22:
            output("Good Evening")
        
        else:
            output("Up late again, you should be sleeping")
            
