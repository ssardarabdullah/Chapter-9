Question 6________
 Store the User class in one 
module, and store the 
Privileges and Admin classes 
in a separate module. In a separate
    file, create an Admin instance and call 
    show_privileges() to show that
    everything is still 



solution ______________





class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")
        

from user_module import User

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
        

from admin_module import Admin

admin_user = Admin("Admin", "Boss")
admin_user.privileges.show_privileges()
