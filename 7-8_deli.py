# Name: Mariam Shatta
# Course: CSCI-1511
# Participation Activity 1
# Exercise 7-8: Deli

sandwich_orders = ['tuna', 'turkey', 'chicken', 'ham']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)
