def main():
    try:
        n = int(input("Enter a positive integer: "))
        
        if n <= 0:
            print("Error: Please enter a positive integer.")
            return
        
        for i in range(-n, n + 1):
            if i != 0:
                print(i)
    except ValueError:
        print("Please enter a positive integer")

main()
