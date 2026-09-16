# Name: Mariam Shatta
# Course: CSCI-1511
# Participation Activity 1
# Exercise 7-9: No Pastrami

sandwich_orders = [
    'tuna', 'pastrami', 'turkey',
    'pastrami', 'chicken', 'pastrami', 'ham'
]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)
