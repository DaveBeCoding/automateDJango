#! /usr/bin/python3

import os 
import time
import subprocess
import datetime
from default_locate import *

def location_menu():
    clear()
    # pause(timer_three)
    choices = input("Select which location you would like your project to be saved \n"
                    
                    "1) Default location ~/dev/django/<project name>/ \n"
                    "2) Current working directory \n"
                    "3) New location \n"
                    
                    )
    clear()
    create_project(choices)
    pause(timer_three)
    
def create_project(chc):
    clear()
    name = project_name()
    pause(timer_three)
    if int(chc) == opt_one:
        # spin_up_django(name)
        create_file(name)
    elif int(chc) == opt_two:
        path = os.getcwd() #pwd
        print("current location: " + path)
        pause()
    elif int(chc) == opt_three:
        new_location = input("type location to place file"
                             
                             " Example: "
                             "~/dev/my_folder"
                             )
 
        pause(timer_three)



def create_file(name):
    clear()
    spin_up_django(name)
    # os.chdir(records) #change dir
    # f= open("r_sheet.txt","w+")
    # f.write(default_test+name)
    # # for i in range(10):
    # #     f.write("This is line %d\r\n" % (i+1))
    # f.close()
    # print(" file at "+ default_test+name +" was successfully created")
    # pause(timer_five)


def project_name():
    p_name = input( " Enter project name \n")
    return p_name
    

def spin_up_django(name):
    project_name = default_test+name
    makeDir(project_name)
    changeDir(project_name)
    os.system(virtualenv_create)
    changeDir(project_name)
    # os.system(source_bin)
    makeDir(s_r_c)
    changeDir(s_r_c)
    # activate_venv(project_name)


def main():
    location_menu()
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pause(set_time):
    time.sleep(set_time)
    
def makeDir(dir):
    os.mkdir(dir)
    
def changeDir(cdir):
    os.chdir(cdir)  
    
def read_file():
    pass
    
def activate_venv(p_name):
    changeDir(p_name)
    pause(timer_three)
    clear()
    os.system("bashScript.sh") #this runs the script
    # subprocess.Popen("bashScript.sh") #this works
    
if __name__ == "__main__":
    main()