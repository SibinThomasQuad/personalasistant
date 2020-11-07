#!/usr/bin/python3.6
import pymysql
def db_connection():
    mydb = pymysql.connect("localhost","sibin","darkcoder","my_asistance" )
    mycursor = mydb.cursor()
    return mycursor
