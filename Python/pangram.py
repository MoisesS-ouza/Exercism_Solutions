def is_pangram(sentence: str) -> bool:
    '''Determines if a sentence is a pangram (if it uses all the 26 letters of the alphabet)
    
    :param sentence: Sentence to be checked
    :type sentence: str
    '''
    sentence = ''.join(sentence.split())
    letter_list = []
    
    for letter in sentence:
        if letter.isalpha():
            if letter.lower() not in letter_list:
                letter_list.append(letter.lower())

    if len(letter_list) == 26:
        return True

    return False

print(is_pangram('The quick brown fox jumps over the lazy dog'))