user_list = []
print("Enter numbers to sort them. Enter 0 to stop.")

while True:
        number = int(input("Enter a number: "))
       

        if number == 0:  
            print("Goodbye")
            break

        user_list.append(number)
        print("Current List:", user_list)
        print("Sorted List:", sorted(user_list))
 