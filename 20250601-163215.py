import random

# Create a list of 10 numbers and 5 letters
lottery_items = list(range(10)) + list("ABCDE")

# Randomly choose 4 items
winning_ticket = random.sample(lottery_items, 4)

print(f"Any ticket matching these four numbers or letters wins a prize: {winning_ticket}")