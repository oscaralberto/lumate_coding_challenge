lumate_coding_challenge
===========================================================

-The Repository Directory contains one Folder named mysite1.
This directory contains all the files needed to build my 
basic website. 

-It has been connected to a postgresql database named 'mydb2'
with user 'myfirstuser' and user password 'gominers13'

-The website is created through a Django ModelForm. Each 
guestbook entry has a name, surname and date(of creation),
but only name and surname are rendered in the form. 

-The Django admin website has been activated as well. It 
can be accessed at http://127.0.0.1:8000/admin 
The admin user is 'oscar' with password 'gominers13' 

-The main local url for the website is(considering 
the command "python manage.py runserver" has been
executed previously:
http://127.0.0.1:8000/guestbooks
It will display a simple page with two forms to enter a
first and last name. Once the information was submitted, it
will take the user to a page informing of a successfull 
submission. This page contains two links to go back to the 
main page or see who else has signed the guestbook.



