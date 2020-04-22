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