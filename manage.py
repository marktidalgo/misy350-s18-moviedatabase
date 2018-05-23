from flask_script import Manager
from moviebase import app, db, Actor, Movie

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    tomcruise = Actor(name='Tom Cruise', about='American Action Star')
    annehathaway = Actor(name='Anne Hathaway', about='A-list Movie Star')
    bradpitt = Actor(name='Brad Pitt', about='American Movie Star')
    movie1 = Movie(name='Mission Impossible', year=1996, producer="Paula Wagner", actor=tomcruise)
    movie2 = Movie(name='Devil Wears Prada', year=2006, producer="Wendy Finerman", actor=annehathaway)
    movie3 = Movie(name='Fight Club', year=1999, producer="Art Linson", actor=bradpitt)
    db.session.add(tomcruise)
    db.session.add(annehathaway)
    db.session.add(bradpitt)
    db.session.add(movie1)
    db.session.add(movie2)
    db.session.add(movie3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
