import unittest
from app.models import Review,User
from flask_login import current_user
from app import db

class TestReview(unittest.TestCase):

    '''
    Test class facilitates the creation of new test units
    '''
    def setUp(self):

        '''
        Method runs before every test case
        '''
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_review = Review(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James )
    
    def tearDown(self):

        '''
        Method runs after every test and deletes content to ensure the accuracy of tests
        '''
        Review.query.delete()
        User.query.delete()
    
    def test_save_review(self):

        '''
        Test case checks if reviews are saved in the database
        '''
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)
    def test_check_instance_variables(self):

        '''
        Test case checks if objects are initialized correctly
        '''
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.movie_title,'Review for movies')
        self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_James)
    
    
    

    def test_get_review_by_id(self):
        
        '''
        Test checks if database returns saved reviews
        '''
        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)