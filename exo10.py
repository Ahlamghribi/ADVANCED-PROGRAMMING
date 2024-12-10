phrase = input("Please type a word or phrase: ").replace(" ", "").lower() 
is_palindrome = True

for i in range(len(phrase) // 2):
    if phrase[i] != phrase[-(i + 1)]:
        is_palindrome = False
        break 

if is_palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
