class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return list({review.get_customer() for review in self.reviews})

    def average_star_rating(self):
        if not self.reviews:
            return 0
        return sum([review.get_rating() for review in self.reviews]) / len(self.reviews)

    @classmethod
    def get_all_restaurants(cls):
        return cls.all_restaurants


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
        self.restaurant.reviews.append(self)

    def get_rating(self):
        return self.rating

    def get_customer(self):
        return self.customer

    def get_restaurant(self):
        return self.restaurant


class Customer:
    def __init__(self, full_name, given_name):
        self.full_name = full_name
        self.given_name = given_name

    def __str__(self):
        return self.full_name
