from Pages_Amazon.login import Login
from Pages_Amazon.home import Home
from Pages_Amazon.product_listing import ProductListing
from Pages_Amazon.address_page import AddressPage


class User(Home, Login, ProductListing, AddressPage):
    def _init_(self, driver):
        self.driver = driver
        print("hey")

    def print_user(self):
        print("im user")




