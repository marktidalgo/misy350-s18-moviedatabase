# misy350-s18-moviedatabase
The final project repo for Mark Tidalgo.

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
## Database Design

The database consists of two tables, Actors and Movies. The Actors table has the following fields of information: Actor ID, Name, and a Brief Bio of that actor. The Movie table has the following fields of information: 
