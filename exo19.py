def unique_word_counter():
    unique_words = set() 
    total_words = 0 

    while True:
        word = input("Enter a word: ").strip()   
        if word in unique_words:
            print(f"You typed in {len(unique_words)} unique words.")
            break
        unique_words.add(word)  
        total_words += 1  

unique_word_counter()
