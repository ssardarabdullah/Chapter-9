Question 9______
You can use a loop to see how
hard it might be to win
the kind of lottery you just 
modeled. Make a list or tuple
called my_ticket.
Write a loop that keeps pulling
numbers until your ticket wins.
Print a messagereporting how many times the loop
had to run to give you a winning 
ticket.

solution _________
my_ticket = random.sample(lottery_items, 4)
attempts = 0
while True:
    new_ticket = random.sample(lottery_items, 4)
    attempts += 1
    if set(new_ticket) == set(my_ticket):
        brprint(f"Winning ticket matched after {attempts} attempts!")
