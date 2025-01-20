def anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

print(anagrams("tame", "meta"))  # True
print(anagrams("tabby", "batty"))  # False
