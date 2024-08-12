print('Welcome to the tip calculator!')
bill = float(input("What was the total bill: "))
percent = int(input('How much tip would you like to give [10, 12, or 15]: '))
people = int(input('How many people to split the bill: '))

# Calculate the total bill including the tip
total_bill = bill + (bill * (percent / 100))

# Divide the total bill by the number of people
total_per_person = total_bill / people

print(f'Each person should pay: ${total_per_person:.2f}')
