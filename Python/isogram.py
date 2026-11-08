'''
An isogram (also known as a "non-pattern word") 
is a word or phrase without a repeating letter, 
however spaces and hyphens are allowed to appear multiple times.
'''

def is_isogram(phrase: str) -> bool:
    '''Determines if a phrase is an isogram. Returs True if so
    
    :param phrase: Phrase to be checked
    :type phrase: str
    '''
    letters = ''
    for letter in phrase:
        if letter.isalpha():
            if letter.lower() not in letters:
                letters += letter.lower()
            else:
                return False

    return True

print(is_isogram('six-year-old'))