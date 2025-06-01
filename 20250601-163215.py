Question 8______
 You can use a loop to see how hard 
it might be to win
the kind of lottery you just
modeled. Make a list or tuple 
called my_ticket.
Write a loop that keeps pulling 
numbers until your ticket wins. 
Print a messagereporting how many times the loop 
had to run to give you a winning
ticket.


solution _________
import random
lottery_items = list(range(10)) + list("ABCDE")
winning_ticket = random.sample(lottery_items, 4)
print(f"Any ticket matching these four numbers or letters wins a prize: {winning_ticket}")
