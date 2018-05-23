# misy350-s18-moviedatabase
The final project repo for Mark Tidalgo.

## Database Design

The database consists of two tables, Actors and Movies. The tables are related in a one-to-many relationship as a single actor can be the lead in multiple movies. The Actors table has the following fields of information: Actor ID, Name, and a Brief Bio of that actor. The Movie table has the following fields of information: Movie ID, Title, Lead Actor, and Producer. You may view the table layouts below:

### Artists:

#|Name|About|Edit|
------------|-------------
1 | Tom Cruise    | American Action Star | 'Edit' 'Delete' 'Delete Ajax'
2 | Anne Hathaway | A-list Movie Star    | 'Edit' 'Delete' 'Delete Ajax'
3 | Brad Pitt     | American Movie Star  | 'Edit' 'Delete' 'Delete Ajax'

### Movies:

#|Name|Year|Lead Actor|Producer|Edit|
------------|-------------
1 | Mission Impossible | 1996 | Tom Cruise    | Paula Wagner   | 'Edit' 'Delete' 'Delete Ajax'
2 | Devil Wears Prada  | 2006 | Anne Hathaway | Wendy Finerman | 'Edit' 'Delete' 'Delete Ajax'
3 | Fight Club         | 1999 | Brad Pitt     | Art Linson     | 'Edit' 'Delete' 'Delete Ajax'




## Front-End Design

The navbar incorporated by Bootstrap can take the user to any page in the web application, no matter what page the user is currently on. Click the Film logo to go to the Homepage, 'Artists' to look at all the artists in the database, 'Movies' to view all the Movies in the database and 'About' to view my information.


## Setup Instructions:

Make sure to use Python version 2.7.x.

Install `virtualenv` if needed.

If you do not have a virtual environment yet on the project folder, set it up with:

    $ virtualenv venv

Then activate the virtual environment

    $ source venv/bin/activate

Install packages

    $ pip install -r requirements.txt

To initialize the database:

    $ python manage.py deploy

To run the development server (use `-d` to enable debugger and reloader):

    $ python manage.py runserver -d

## Movie Database Application Instructions:

Once you have ran the server you may access the application at:

     http://127.0.0.1:5000/
