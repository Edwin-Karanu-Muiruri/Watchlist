from flask import render_template #A function that takes in the name of a template file as a first argument, then automatically searches for the template file in our app/templates/sub directory.
from app import app

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'Home - Welcome to The Best Movie Review Website Online'
    return render_template('index.html', title = title)
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data.
    '''
    return render_template('movie.html', id = movie_id)