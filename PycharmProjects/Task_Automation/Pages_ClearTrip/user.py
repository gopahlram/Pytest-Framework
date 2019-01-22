'''
Common method which inherit all other file methods and User can access all methods
from test case using this class
'''


from Pages_ClearTrip.login import Login
from Pages_ClearTrip.home import Home
from Pages_ClearTrip.flight_booking import FlightBooking
from Pages_ClearTrip.flight_listing import FlightListing


class User(Home, Login, FlightListing, FlightBooking):
    def _init_(self, driver):
        self.driver = driver



