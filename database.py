import sqlite3

#creates connction with database
def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection

#get all queestionsAndAnswers tuples  from database
def get_questions_and_answers():
    con = create_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM questionsAndAnswers")
    return cur.fetchall()

#get specific questionsAndAnswers tuple value from database
def get_answers_from_memory(question):
    rows = get_questions_and_answers()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break
    
    return answer

#insert a questionsAndAnswer tuple in database
def insert_questions_and_answers(question,answer):
    con = create_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO questionsAndAnswers values('"+question+"','"+answer+"')")
    con.commit()

def update_last_seen(today_date):
    con = create_connection()
    cur = con.cursor()
    cur.execute("UPDATE keysAndValues SET date = ? WHERE PreviousDate = ?",(today_date, "previous_date"))
    con.commit()

def get_last_seen():
    con = create_connection()
    cur = con.cursor()
    data = str(cur.execute("SELECT date FROM keysAndValues WHERE PreviousDate = ?",("previous_date",)).fetchone()[0])
    return data

















