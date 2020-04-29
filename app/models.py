from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):

    '''
    function queries and returns user with a give id
    '''
    return User.query.get(int(user_id))

class Movie:

    '''
    Movie class to define movie obects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):

        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count

class Review:

    '''
    Class creates review objects
    '''

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):

        '''
        method initializes a review
        '''
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):

        '''
        method saves added reviews to the all_reviews list
        '''
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):

        '''
        method deletes reviews
        '''
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        '''
        method displays available reviews
        '''

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response

class User(UserMixin,db.Model):

    '''
    Function facilitates the creation of new users
    '''
    #give proper name to tables in database
    __tablename__ = 'users'
    #create id table column
    id = db.Column(db.Integer,primary_key=True)
    #create name column
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    #create connection between roles and users
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path =  db.Column(db.String())
    #a Foreign key is a field in one table that references a primary key in another table
    pass_secure = db.Column(db.String(255))
    #pasword column
    #function facilitates debugging
    def __repr__(self):
        return f'User {self.username}'
    
    @property
    def password (self):

        '''
        Function blocks access to password property
        '''
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):

        '''
        Function generates and passes hashed password
        '''
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):

        '''
        Function takes password, hashes it, and compares it to hashed password
        '''
        return check_password_hash(self.pass_secure,password)

    


    

class Role(db.Model):

    '''
    Function to determine the level of access that users have
    '''
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")
    #The first argument is the class that we are referencing which is User. Next backref allows us to access and set our User class. We give it the value of role now because when we want to get the role of a user instance we can just run user.role. Lazy parameter is how SQLAlchemy will load our projects. The lazy option is our objects will be loaded on access and filtered before returning (Moringa,2017).

    def __repr__(self):
        return f'User {self.name}'

