#!/usr/bin/python3.6
import os
from operations_data import *
from recorder import *
import gtts
from playsound import playsound
from db_connection import *
#mysql connection
mycursor = db_connection()
#colors
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'
#colors
def learning_mode(ques):
    #my_question=record()
    answer_study=record()
    #learning process
    sql = "INSERT INTO brain (qustion, answer) VALUES (%s, %s)"
    val = (ques, answer_study)
    mycursor.execute(sql, val)
    confirmation="Ok i will remember that";
    print(">>"+confirmation)
    speak(confirmation)
def speak(my_text):
    tts = gtts.gTTS(str(my_text))
    tts.save(str(my_text)+".mp3")
    playsound(str(my_text)+".mp3")
    os.remove(str(my_text)+".mp3") 
def get_answer(question):
    mycursor.execute("SELECT answer FROM brain where qustion LIKE '%"+question+"%'")
    myresult = mycursor.fetchall()
    data_count=len(myresult)
    if data_count > 0:
        flag=0
        for x in myresult:
            print(green(">>"+str(x[0])))
            speak(x)
        ask_question()
    else :
        mycursor.execute("SELECT qustion FROM brain where answer LIKE '%"+question+"%'")
        myresult = mycursor.fetchall()
        data_count_reverse=len(myresult)
        if data_count_reverse > 0:
            flag=1;
            for y in myresult:
                print(green(">>You said that"+question+" is the answer for"+str(y[0])))
                speak("You said that   "+str(question)+" is the answer for"+str(y[0]))
                ask_question()
        else:
            appology='Sorry i dont know if you said i will remember that\n'
            print(green('>>'+appology))
            speak(appology)
            learning_mode(question)
            ask_question()
def ask_question():
    my_question=record()
    if my_question=='bye':
        speak('Ok bye see you later')
        print('Ok bye see you later')
        quit()
    else:
        task_seprate=my_question.split(" ", 1)
        tasker=task_seprate[0]
        mycursor.execute("SELECT fuctions FROM tasks where operations LIKE '%"+tasker+"%'")
        myresult_task = mycursor.fetchall()
        data_count_reverse_task=len(myresult_task)
        if data_count_reverse_task > 0:
            parameters=task_seprate[1]
            for z in myresult_task:
                fuction_task=z[0]
                method = eval(fuction_task)
                args = [parameters]
                process_result=method(str(parameters))
                if process_result is None:
                    speak("Ok i will do that")
                else:
                    speak("the answer is "+str(process_result))
                    print(green(">>the answer is "+str(process_result)))
                #namer('sibin')
                ask_question()
        #search tasker in db
        #search tasker in db
        get_answer(my_question)
ask_question()

