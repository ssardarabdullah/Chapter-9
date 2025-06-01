Question 5______
Store the classes User,
Privileges, and Admin in one 
module. Create a sepa￾rate file, 
make an Admin instance, and call 
show_privileges() to show that 
everything is working correctly.

solution _________
    class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
  def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
 def greet_user(self):
        print(f"Hello, {self.first_name}!")
class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]
 def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
