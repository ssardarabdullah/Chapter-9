Question 4________

 Using your latest Restaurant
class, store it in a mod￾ule. 
Make a separate file that imports
Restaurant. Make a Restaurant
instance, and call one of
Restaurant’s methods to show that 
the import statement is work￾ing
properly

Solution __________
class Restaurant:
 def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
 def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
 def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
        from restaurant import Restaurant
my_restaurant = Restaurant("Sunset Grill", "Barbecue")
my_restaurant.describe_restaurant()
