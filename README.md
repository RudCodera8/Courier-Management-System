# Courier Management System 
Courier Management System is a project that I have made as a part of Amfoss-A batch project. This project will help the courier receivers 
to know whether their couriers have reached the mail room at Amritapuri. Though the project is incomplete in terms of user interface and 
user experience, I have made sure that there are no problems in the project at this stage. For making this project I have selected Django as the framework.
Here are the steps I have been through for making this project. 
***

## Technology Stack Used  
[Django](https://www.djangoproject.com/) The Web Framework used .

[Python 3](https://www.python.org/) - Built With.

## OverView Of The Project 
This is A Courier Management System where the admin will enter receiver details (name, roll_number, service) when the package has reached the mail room. 
After admin enters all the details, it will be stored in the database. The user will enter his/her above given details and check whether the package has reached or not. 

## Things That Worked 
As per the conditions, I tried to create a admin login page and database for storing details for some fields(could not include date of receiving).
Created a user search page user for searching the database using the given details and it prints the details in the database. 

## Things That Did not Work Out
The need for login page for user is not necessary as per the functionality , because the user only needs to know whether his package has reached the mail room or not.
So I did not include user login page . And for user courier search page I could not find a way to include a link that links to the search page in the admin login page.
The evaluator will have to enter search/ after the host id to manually access the search page. 

## Future Plans for the project. 
I would like to improve the UI/UX of the webpage, include easy access of user page from the admin login page itself. In short I would like to give it a professional look.   


# Instructions And steps for Creating the project. (How I created this project.)

### Installation Of Django

***
Before Installing Django , make sure your system has python3.x , we will be working on python3 throughout the project. 
Type the following in your terminal window to check the default version of python. 
```
$ python -v
```
If you are viewing python 2.x after entering the above command follow next steps carefully.

#### Creating a virtual environment. 
In order to create an environment where we will have python 3 as our default version(no need of typing python3)
follow these steps.
##### 1)Make a directory in which we will save our project and change your current working directory to that folder.
```
$ mkdir yourfilename      ==> In my case , filename is project.
$ cd yourfilename         
```
##### 2)Virtual Environment 
```
$ virtualenv  -p python3          ==> Creates a virtual environment for the current directory to run python3 as default.
```
##### 3) Activating The Virtual Environment

To activate the virtual environment type the following command . This will come in use many at times. 

```
$ source bin/activate               (for deactivating  ==> deactivate)
```

#### Installing Django inside the virtual environment. 

Once you have activated the virtual environment, install Django 2.0.7 using the following command 
```
$ pip install django==2.0.7 
```
Enter the following to view all the components of your virtual environment.
```
$ pip freeze
```
YOU HAVE SUCCESSFULLY INSTALLED DJANGO IN YOUR SYSTEM AS IN YOUR VIRTUAL ENVIRONMENT. 


Once you have django installed you will find some files (namely bin, include and lib) included in your directory. 

## Creating the project. 
Since this is the documentation of how I made the project, I will be using terms that are not conventional. So please take time to read the Django Documentations.

#### 1) Creating a project . 
Create a directory of any name and change into that directory . We will be creating the project there. 
```
$ mkdir courier
```
In Django to create a project the command used is 
```
$ django-admin startproject courier .
```

You will find two files if you list the directory . (namely yourprojectname and manage.py)

To ensure everything is working correctly type this in your terminal 
```
$ python manage.py runserver 
```
A port link will be there on your screen click on that and it will redirect you to Django Official page with a Rocket on it stating The installed worked Successfully.

Some things to remember all throughout 

##### Makemigrations & Migrations
This make changes to your models and fields without changing your databases. 

To makemigrations and migrate type the following commands. 
```
$ python manage.py makemigrations
$ python manage.py migrations
```

##### Runserver (LocalHost)
To runserver i.e. create a local host which helps us to preview the created project.

```
$ python manage.py runserver
```

#### Setting up your code editor. 
Setting up your code editor with your root folder is absolutely necessary while creating the Django project because it will be easy to edit code directly. 
In my case, I used Sublime Text throughout the project for editing code. 



## Basic Functionalities of Django. 

When you will open the project folder , you can view three python files, namely settings.py, urls.py, wsgi.py . 
These are the main pages which helps in the functioning of Django. 
If we open settings,  we can view many settings available for us to access to make our project. 
The important ones are INSTALLED_APPS and TEMPLATES , which will be the settings we are gonna make use of. 

***
## Creating an Admin. 
In order to move forward, we need an Admin who will monitor the working and maintaining the databases. For this an Admin is required. 
To create an Admin : 
```
$ python manage.py createsuperuser 
```
This will redirect you to inputs asking for username , password and email address . 
This will be the Admin details you are reqiured to put while login . 

To get an Idea of how it works : runserver and try to login with the credentials you have provided . 
You will be given authentication to the whole database. 


## Creating An App 
Apps are the main modules which make your page. Assume that as a webpage that is made for conducting only one function. 
To create an App
```
$ python manage.py startapp yourappname
in my case : python manage.py startapp mainpage           ==> for database management(inshort for models)
           : python manage.py startapp pages              ==> for templates and views. 

```
After Creating an app it is mandatory to register you app to the INSTALLED_APP section of settings.py. Always make sure to do the same.
Here you can view my [settings.py](https://github.com/RudCodera8/Courier-Management-System/blob/master/project/courier/courier/settings.py) file and search for mainpage and pages which are apps that I have registered in INSTALLED_APPS section.

## Models 
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. 
Generally, each model maps to a single database table. We can create models according to our requirement, which will be some type of data that will be stored to the database. 
For reading more about [Models](https://docs.djangoproject.com/en/2.2/topics/db/models/) - Django Documentation. 
There are many types of modelFields, I have used Character Field more because I thought it was the only ModelField that was flexible. 

After making changes to the models.py always register your models to the admin.py file. This ensures your modelFields will appear on the admin handle

See the [models.py](https://github.com/RudCodera8/Courier-Management-System/blob/master/project/courier/mainpage/models.py) that I have used as part of the project.

View my [admin.py](https://github.com/RudCodera8/Courier-Management-System/blob/master/project/courier/mainpage/admin.py) file here, where I registered the model class student. 

## Templates And Views. 
Templates area the layout of the web page written in Html. A view is a callable which takes a request and returns a response. This can be more than just a function, and Django provides an example of some classes which can be used as views.

For this project I made a folder in the main root directory namely templates(not a convention but a good practice.) and register the path of the template folder in the settings TEMPLATES field and saved the search.html which is the integral part of the user Courier service tracker.
You can view the contents of [templates](https://github.com/RudCodera8/Courier-Management-System/tree/master/project/templates) folder. 

This is the [search.html](https://github.com/RudCodera8/Courier-Management-System/blob/master/project/templates/search.html) I have written to search the database .


## Urls
This is one of the main components of Django. The file urls.py registers the availabe urls to the corresponding views . 
You can have a look at my [urls.py](https://github.com/RudCodera8/Courier-Management-System/blob/master/project/courier/pages/views.py) in the pages app. Also I have created a View which searches the database for \
matching information that the user has given as input. Also during registering urls it is mandatory to import the required modules. 

***
***
# How I Created The Project. 
## Step1
Creation of Virtual Environment.
Installing Django .
Up and Running Of Django Basics like Migrations and Runserver . 

## Step 2 
Starting A project.
Starting 2 Apps.(mainpage and pages)

## Step 3 
Creating an Admin.
Creating Basic Models and trying to enter Data using Admin site.

## Step 4
Editing The Admin Site using basic operations in admin.py

## Step 5
Writing the code for [search.html](https://github.com/RudCodera8/Courier-Management-System/blob/master/project/templates/search.html) which displays the user details.
Preparing the views and templates for the main page in [views.py](https://github.com/RudCodera8/Courier-Management-System/blob/master/project/courier/pages/views.py).

## Step 6
Editing Urls and finally registering and importing required modules. 




## References 
[Django Documentation](https://docs.djangoproject.com/en/2.2/) - Django CookBook.
[StackOverFlow](https://stackoverflow.com/) - For Solving Errors.
YouTube Videos Helped upto some extent to solve some errors. 









































