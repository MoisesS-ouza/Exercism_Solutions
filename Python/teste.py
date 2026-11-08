def move_initial_consonants(word):
    vowels = "aeiouAEIOU"
    
    # Track the position of the first vowel
    for index, char in enumerate(word):
        if char in vowels:
            # Cut from the vowel to the end + from the start up to the vowel
            return word[index:] + word[:index]
            
    # If the word has no vowels at all, return it as is
    return word

print(move_initial_consonants('pig'))
