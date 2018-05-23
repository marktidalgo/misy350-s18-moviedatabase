import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    about = db.Column(db.Text)
    movies = db.relationship('Movie', backref='actor', cascade="delete")


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    year = db.Column(db.Integer)
    producer = db.Column(db.String(256))
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'))


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return render_template('index.html')


@app.route('/actors')
def show_all_actors():
    actors = Actor.query.all()
    return render_template('actor-all.html', actors=actors)


@app.route('/actor/add', methods=['GET', 'POST'])
def add_actors():
    if request.method == 'GET':
        return render_template('actor-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        about = request.form['about']

        # insert the data into the database
        actor = Actor(name=name, about=about)
        db.session.add(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))


@app.route('/api/actor/add', methods=['POST'])
def add_ajax_actors():
    # get data from the form
    name = request.form['name']
    about = request.form['about']

    # insert the data into the database
    actor = Actor(name=name, about=about)
    db.session.add(actor)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Actor Inserted', 'success')
    return jsonify({"id": str(actor.id), "name": actor.name})


@app.route('/actor/edit/<int:id>', methods=['GET', 'POST'])
def edit_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-edit.html', actor=actor)
    if request.method == 'POST':
        # update data based on the form data
        actor.name = request.form['name']
        actor.about = request.form['about']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_actors'))


@app.route('/actor/delete/<int:id>', methods=['GET', 'POST'])
def delete_actor(id):
    actor = Actor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('actor-delete.html', actor=actor)
    if request.method == 'POST':
        # delete the actor by id
        # all related songs are deleted as well
        db.session.delete(actor)
        db.session.commit()
        return redirect(url_for('show_all_actors'))


@app.route('/api/actor/<int:id>', methods=['DELETE'])
def delete_ajax_actor(id):
    actor = Actor.query.get_or_404(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({"id": str(actor.id), "name": actor.name})


# song-all.html adds song id to the edit button using a hidden input
@app.route('/movies')
def show_all_movies():
    movies = Movie.query.all()
    return render_template('movie-all.html', movies=movies)


@app.route('/movie/add', methods=['GET', 'POST'])
def add_movies():
    if request.method == 'GET':
        actors = Actor.query.all()
        return render_template('movie-add.html', actors=actors)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        year = request.form['year']
        producer = request.form['producer']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie = Movie(name=name, year=year, producer=producer, actor=actor)

        # insert the data into the database
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movie/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    actors = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-edit.html', movie=movie, actors=actors)
    if request.method == 'POST':
        # update data based on the form data
        movie.name = request.form['name']
        movie.year = request.form['year']
        movie.producer = request.form['producer']
        actor_name = request.form['actor']
        actor = Actor.query.filter_by(name=actor_name).first()
        movie.actor = actor
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/movie/delete/<int:id>', methods=['GET', 'POST'])
def delete_movie(id):
    movie = Movie.query.filter_by(id=id).first()
    actors = Actor.query.all()
    if request.method == 'GET':
        return render_template('movie-delete.html', movie=movie, actors=actors)
    if request.method == 'POST':
        # use the id to delete the movie
        # movie.query.filter_by(id=id).delete()
        db.session.delete(movie)
        db.session.commit()
        return redirect(url_for('show_all_movies'))


@app.route('/api/movie/<int:id>', methods=['DELETE'])
def delete_ajax_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({"id": str(movie.id), "name": movie.name})


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/users')
def show_all_users():
    return render_template('user-all.html')


@app.route('/user/<string:name>/')
def get_user_name(name):
    # return "hello " + name
    # return "Hello %s, this is %s" % (name, 'administrator')
    return render_template('user.html', name=name)


@app.route('/movie/<int:id>/')
def get_movie_id(id):
    # return "This song's ID is " + str(id)
    return "Hi, this is %s and the movie's id is %d" % ('administrator', id)


# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
