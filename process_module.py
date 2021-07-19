#module to process input
from output_module import output
from date_time_module import get_time,get_date
from database import get_answers_from_memory, insert_questions_and_answers
from input_module import take_input
from internet_module import cheack_inteternet_connection, check_wiki
import websites
#process input to give command values like 'get time details' to know current time 
def process(query):
    answer = get_answers_from_memory(query)


    
    if answer == "get time details":
        return ("Current time is " + get_time())


  
    elif answer == "check internet connection":
        if cheack_inteternet_connection():
            return "Internet is connected"
        else:
            return "Internet is not connected"



    elif answer == "get todays date":
        return ("Todays date is " + str(get_date()))

    elif answer == "open google":
        websites.get_google()
        return "opening google"

    elif answer == "open facebook":
        websites.get_facebook()
        return "opening facebook"

    elif answer == "watch anime":
        websites.get_animixplay()
        return "opening animixplay"

    elif answer == "open geeksforgeeks":
        websites.get_geeksforgeeks()
        return "opening Geeks for Geeks"

    elif answer == "open stackoverflow":
        websites.get_stackoverflow()
        return "opening Stack Overflow"

    elif answer == "open youtube":
        websites.get_youtube()
        return "opening youtube"

    elif answer == "open instagram":
        websites.get_instagram()
        return "opening instagram"

    elif answer == "open whatsapp":
        websites.get_whatsapp()
        return "opening whatsapp"

    elif answer == "open reddit":
        websites.get_reddit()
        return "opening reddit"



    #teach assistanant new commands    
    else:
        
        output("I dont know this one. Do you want to search online?")
        ans = take_input()
        if "yes" in ans:
            answer = check_wiki(query)
            if answer != "":
                 return answer
        else:         
            output("Then tell me what it means.I will remember for next time.")
            ans = take_input()
            # 'it means' is used to tell computer that we are telling the meaning of the unknown command
            if "it means" in ans:
                ans = ans.replace("it means","")
                ans = ans.strip()#to strip extra space i.e " " after 'it means' and before meaning of the command task
                value = get_answers_from_memory(ans)
                if value == "":
                    return "cant help with this one"
                else:
                    insert_questions_and_answers(query,value)
                    return "i will remember that for next time"
            else:
                return "cant help with this one"
                
            