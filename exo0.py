
people = int(input("How many people need a ride? "))
capacity = int(input("How many people fit in one taxi? "))

full_taxis = people // capacity

if people % capacity != 0:
    full_taxis += 1
 
print(f"Number of taxis needed: {full_taxis}")
 
print("This program calculates the number of taxis based on the group's size and taxi capacity.")
print("Even if only one person is left after filling the taxis, an extra taxi is accounted for.")
