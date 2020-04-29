from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required
#import blueprint
from . import main

from ..request import get_movies, get_movie, search_movie

#import Review and ReviewForm classes
from ..models import Review,User
from .forms import ReviewForm
Review = Review

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''


    # Getting popular movies
    popular_movies = get_movies('popular')
    # Getting upcoming movies
    upcoming_movie = get_movies('upcoming')
    # Getting now playing movies
    now_showing_movie = get_movies('now_playing')

    title = "Watchlist"

    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('main.search', movie_name = search_movie))
    else:
        return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

    

    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

    #The first title on the left of the = sign, represents the variable in the template. While the one to the right represents the variable in our view function.
    

@main.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''

    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)
    
    return render_template('movie.html',title = title, movie = movie, reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name):

    '''
    View function to display the search results i.e. the movie that a user is searching for
    '''

    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'Search results for {movie_name}'
    return render_template('search.html', movies = searched_movies, title = title)

@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required
#decorator ensures that only authenticated users can post moview reviews
def new_review(id):

    '''
    View function to display review form and form input
    '''

    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('main.movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form = form, movie = movie)

@main.route('/user/<uname>')
def profile(uname):

    '''
    Function returns user's profile page if a user exits or return 404 error if the user does not exist in the data base
    '''
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    return render_template("profile/profile.html", user = user)