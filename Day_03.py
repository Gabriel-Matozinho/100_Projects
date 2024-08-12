price = 0.0
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want [S, M, L]: ").upper()

if size == 'S':
    price += 15
    pepperoni = input("Add pepperoni for small pizza [Y or N]: ").upper()
    if pepperoni == 'Y':
        price += 2

elif size == 'M':
    price += 20
    pepperoni = input("Add pepperoni for medium pizza [Y or N]: ").upper()
    if pepperoni == 'Y':
        price += 3

elif size == 'L':
    price += 25
    pepperoni = input("Add pepperoni for large pizza [Y or N]: ").upper()
    if pepperoni == 'Y':
        price += 3

extra_cheese = input("Do you want extra cheese [Y or N]: ").upper()
if extra_cheese == 'Y':
    price += 1

print(f"Your final bill is: ${price:.2f}")
