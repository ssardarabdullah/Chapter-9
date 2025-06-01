Question 3_______
 Make a class called User. 
Create two attributes called first_
name
and last_name, and then create
several other attributes that are
typically stored
in a user profile. Make a method 
called describe_user() that prints a summary
of the user’s information.
Make another method called
greet_user() that prints
a personalized greeting to the 
user.Create several instances
representing different users,
and call both methodsfor each user.

solution __________
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

 Creating multiple users
user1 = User("abdullah", "sayyam", 30, "@sardarabdullah.com", pakistan")
user2 = User("ali", "niaz", 45, "ali.niaz  gmali.com", "Pakistan")
user3 = User("abdulrehman", "niaz", 28, "ssardarabdulrehman58@gmail "Pakistan")
Call both methods for each user
user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
print()
user3.describe_user()
user3.greet_user()
