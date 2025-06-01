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

# Creating multiple users
user1 = User("Alice", "Johnson", 30, "alice.j@example.com", "New York")
user2 = User("Bob", "Smith", 45, "bob.smith@example.com", "Chicago")
user3 = User("Claire", "Lee", 28, "claire.lee@example.com", "San Francisco")

# Call both methods for each user
user1.describe_user()
user1.greet_user()
print()

user2.describe_user()
user2.greet_user()
print()

user3.describe_user()
user3.greet_user()