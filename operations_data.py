#!/usr/bin/python3.6
import os
def math_calc(formula):
    answer=eval(formula)
    return answer
def execute_command(command):
    print("Ok sure")
    os.system(command)
def open_app(app_name):
    print("ok i will open"+app_name)
    os.system(app_name)
