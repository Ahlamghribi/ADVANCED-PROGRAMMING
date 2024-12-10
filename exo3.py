
total_amount = float(input("Total amount: "))
number_of_items = int(input("Number of items: "))
day_of_week = input("Day of the week: ").strip().lower()

discount = 0

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    discount += 10  
elif day_of_week in ["saturday", "sunday"]:
    discount += 20  
 
if number_of_items > 5:
    discount += 5   
final_price = total_amount * (1 - discount / 100)
 
print(f"Total price after discount: {final_price:.1f} dinars")
