def main():
    numbers = [1, 2, 3, 4, 5]

    def display_menu():
        print("\nMenu:")
        print("1. Append")
        print("2. Insert")
        print("3. Pop")
        print("4. Remove")
        print("5. Sort")
        print("6. Reverse")
        print("7. Search")
        print("8. Save to File")
        print("9. Load from File")
        print("0. Quit")

    def save_to_file():
        try:
            with open("list_data.txt", "w") as file:
                file.write(" ".join(map(str, numbers)))
            print("List saved to list_data.txt.")
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_from_file():
        try:
            with open("list_data.txt", "r") as file:
                data = file.read()
                loaded_numbers = list(map(int, data.split()))
                return loaded_numbers
        except FileNotFoundError:
            print("File not found. Please save the list first.")
        except Exception as e:
            print(f"Error loading file: {e}")

    while True:
        print("\nCurrent List:", numbers)
        display_menu()

        try:
            choice = int(input("Choose an option: ").strip())

            if choice == 0:
                print("Exiting program.")
                break

            elif choice == 1:  # Append
                value = int(input("Enter value to append: ").strip())
                numbers.append(value)

            elif choice == 2:  # Insert
                value = int(input("Enter value to insert: ").strip())
                index = int(input("Enter index: ").strip())
                if 0 <= index <= len(numbers):
                    numbers.insert(index, value)
                else:
                    print("Index out of range.")

            elif choice == 3:  # Pop
                if numbers:
                    index = int(input("Enter index to pop (leave empty for last): ") or -1)
                    if index == -1:
                        numbers.pop()
                    elif 0 <= index < len(numbers):
                        numbers.pop(index)
                    else:
                        print("Index out of range.")
                else:
                    print("List is empty.")

            elif choice == 4:   
                value = int(input("Enter value to remove: ").strip())
                if value in numbers:
                    numbers.remove(value)
                else:
                    print("Value not found in list.")

            elif choice == 5: 
                numbers.sort()

            elif choice == 6:   
                numbers.reverse()

            elif choice == 7:  
                value = int(input("Enter value to search: ").strip())
                if value in numbers:
                    print(f"Value {value} found at index {numbers.index(value)}.")
                else:
                    print("Value not found.")

            elif choice == 8:  
                save_to_file()

            elif choice == 9:   
                loaded_numbers = load_from_file()
                if loaded_numbers is not None:
                    numbers = loaded_numbers

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
