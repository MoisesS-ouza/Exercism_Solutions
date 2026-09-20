'''
The Caesar cipher is a simple shift cipher ]
that relies on transposing all the letters 
in the alphabet using an integer key between 0 and 26.
'''

def rotate(text: str, key: int) -> str:
    '''
    Turns a text into a Caesar's Cipher

    :param text: Text to be converted into a Caesar's Cipher
    :param key: Positions to be walked in an alphabet
    :type text: str
    :type key: int
    '''

    cipher_string = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in text:
        if letter.isalpha():
            if letter == letter.upper():
                if alphabet.index(letter.lower()) + key > 25:
                    cipher_string += alphabet[(alphabet.index(letter.lower()) + key) - 26].upper()
                else:
                    cipher_string += alphabet[alphabet.index(letter.lower()) + key].upper()

            else:
                if alphabet.index(letter) + key > 25:
                    cipher_string += alphabet[(alphabet.index(letter) + key) - 26]
                else:
                    cipher_string += alphabet[alphabet.index(letter) + key]

        else:
            cipher_string += letter

    return cipher_string

print(rotate('omg', 5))
print(rotate('c', 0))
print(rotate('Cool', 26))
print(rotate('The quick brown fox jumps over the lazy dog.', 13))
print(rotate('Gur dhvpx oebja sbk whzcf bire gur ynml qbt.', 13))