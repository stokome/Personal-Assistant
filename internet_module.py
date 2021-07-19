import urllib.request
import wikipedia

def cheack_inteternet_connection():
    try:
        urllib.request.urlopen("http://google.com")
        return True
    except:
        return False

def check_wiki(query):
    query = query.lower()
    query = query.replace("what is","")
    query = query.replace("who is","")
    query = query.replace("do you know","")
    query = query.replace("tell me about","")
    query = query.replace("tell me ","")
    query = query.replace("how can we","")
    query = query.replace("how can i","")
    query = query.replace("help me with","")
    query = query.replace("how to", "")

    query = query.strip()
    try:
        data = wikipedia.summary(query, sentences = 2)
        return data
    except Exception as e:
        return ""





    




         