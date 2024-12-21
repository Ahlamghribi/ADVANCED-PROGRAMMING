def main():
    numbers = [1, 2, 3, 4, 5]
    
    while True:
        try:
            index = input("Enter index (-1 to quit): ")
             
            if not index.isdigit() and index != '-1':
                raise ValueError("Index must be an integer.")

            index = int(index)

            if index == -1:
                print("Exiting program.")
                break

            if index < 0 or index >= len(numbers):
                raise IndexError("Index out of range. Please enter a valid index.")

            new_value = input("Enter new value: ")

            if not new_value.isdigit():
                raise ValueError("New value must be an integer.")

            new_value = int(new_value)

            numbers[index] = new_value
            print(numbers)

        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except IndexError as ie:
            print(f"Invalid index: {ie}")

if __name__ == "__main__":
    main()
