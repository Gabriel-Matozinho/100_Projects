price = 0.0

size = input("What size do you want [S,M or L]: ").upper()
if size == 'S':
    price += 15.0
    pepperoni = input("Add pepperoni in small pizza [Y oir N]: ").upper()
    if pepperoni == 'Y':
        price += 2.0

elif size == 'M':
    price += 20.0
    pepperoni = input("Add pepperoni in medium pizza [Y oir N]: ").upper()
    if pepperoni == 'Y':
        price += 3

if size == 'L':
    price += 25
    pepperoni = input("Add pepperoni in large pizza [Y oir N]: ").upper()
    if pepperoni == 'Y':
        price += 3

extra_cheese = input("Add extra cheese for any size pizza[Y or N]: ").upper()
if extra_cheese == 'Y':
    price += 1

print(f'Bill = {price:.2f}')
