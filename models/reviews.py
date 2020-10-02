class Review:

    all_reviews = []

    def __init__(self, movie_id, title, imageurl, review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
# We create a Review class that has a __init__() method th
# at takes in the Movie ID, The review title, The image URL a
# nd the review itself. We then have a save_reviewmethod that appends\
#  the review object to a class variable all_reviews that is an empty list. 
# We then have a clear_reviews class method that clears all the Items from the list.
