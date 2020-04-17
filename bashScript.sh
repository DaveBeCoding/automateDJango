#!/bin/bash

startdjgo.py
# echo $name_project
# echo 'bash scripts are fun! '

#work'd
input="/home/<your_user>/records/r_sheet.txt"
while IFS= read -r line 
do  
  echo $line  
done < $input  

echo $line







# result=$(return_sh_var.py)
# echo $result

sleep 10s
# cd build_django/
# pwd
# ls -al

# # source bashScript.sh
# # source "./home/<your_user>/dev/dummyLocations/test1/build_django/bin/activate"
# source bin/activate

# sleep 5s
# pip install django==2.0.7
# pip freeze
# cd src && django-admin startproject build_djangoP .
# python manage.py migrate && python manage.py runserver
# build_django
