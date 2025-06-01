# My ticket
my_ticket = random.sample(lottery_items, 4)

# Counter for attempts
attempts = 0

while True:
    new_ticket = random.sample(lottery_items, 4)
    attempts += 1
    if set(new_ticket) == set(my_ticket):
        break

print(f"Winning ticket matched after {attempts} attempts!")