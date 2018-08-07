# Personal Apostila Manager

### Context
My mom is an artist. She has a lot of digital files with patters, guides, models, etc. The sheer amount of files is very hard to manage, so I've created this simple web-app to provide CRUD functions and store the files in a database.

### About the Project
Even though it's made using Django, it was never intended to become a real website (in a proper server). This is meant to be used locally (diminish security risks by not putting it on the Internet), but it shouldn't be hard to deploy, just read Django docs.

## To-Do
[X] CRUD for Apostila (main model)    
[X] CRUD for Project     
[ ] Planner capabilities    
[ ] Login and Logout

## Installation
**Nota**: In Windows systems it's necessary to install Python (version 3) first.

1. Install `virtualenv` for isolated virtual environment
    `sudo apt-get install virtualenv` 
    `pacman -S python-virtualenv`

2. Create a folder for the system
    `mkdir ApostilaManager`

3. Inside the new folder, create the virtualenv
    `virtualenv –p /usr/bin/python3 venv`

4. Initiate virtualenv 
    `source venv/bin/activate` 
    `source venv\Scripts\activate (Windows)`

5. Install required packages
    `pip install -r requirements.txt` 

6. Clone this repository into the folder
    `git clone <this repo>` 

**NOTE** - You will need a user to access certain parts of the system. To create one,
read next section 'create superuser'. Login only once.

## Running the Program
All the commands here should be given from Folder 'ArtHeart' that contains a file named 'manage,py'
- To start the server (locally) - `python manage.py runserver`
- To create a superuser - `python manage.py createsuperuser`
- To migrate db - `python manage.py migrate`

For further info read [Django Documentation](https://docs.djangoproject.com/pt-br/2.0/).

