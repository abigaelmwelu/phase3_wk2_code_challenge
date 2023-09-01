class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def get_rating(self):
        return self.rating

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant

    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews

    @classmethod
    def find_by_name(cls, name):
        for review in cls.all_reviews:
            if review.customer.full_name() == name:
                return review

    @classmethod
    def find_all_by_given_name(cls, name):
        return [review for review in cls.all_reviews if review.customer.given_name == name]

    def num_reviews(self):
        return len(self.all_reviews)


class Customer:
    def __init__(self, full_name, given_name):
        self.full_name = full_name
        self.given_name = given_name

    def __str__(self):
        return self.full_name
