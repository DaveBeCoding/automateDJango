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

cd $line
# cd build_django/ #old static working way

# pwd
ls -al
# sleep 10s

# # # source "./home/<your_user>/dev/dummyLocations/test1/build_django/bin/activate"
source bin/activate

sleep 5s
pip install django==2.0.7
pip freeze
cd src && django-admin startproject build_djangoP .
python manage.py migrate && python manage.py runserver
#build_django



#