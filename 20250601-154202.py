Question 1___________

Make a class called Restaurant.
The init() method for
Restaurant should store two 
attributes: a restaurant_name 
and a cuisine_type.
Make a method called describe_
restaurant() that prints these
two pieces of
information, and a method called
open_restaurant() that prints a 
message indi￾cating that the 
restaurant is open.
Make an instance called restaurant 
from your class. Print the two
attri￾butes individually, and then
call both methods.


solution _________
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

 def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
Creating an instance
restaurant = Restaurant("Ocean Breeze", "Seafood")
 Print attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
 Call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
