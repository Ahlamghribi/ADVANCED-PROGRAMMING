# Program: String in a Frame

# Ask the user for the word
word = input("Word: ")

# Calculate the number of spaces to center the word within the 30-character width
spaces = (30 - len(word)) // 2

# Print the top frame (30 stars)
print('*' * 30)

# Print the line with the word in the center
print('*' + ' ' * spaces + word + ' ' * (30 - len(word) - spaces - 2) + '*')

# Print the bottom frame (30 stars)
print('*' * 30)
