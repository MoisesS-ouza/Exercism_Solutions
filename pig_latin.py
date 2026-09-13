'''
Pig Latin is a made-up children's language that's difficult for non-children to understand.
'''

def translate(text: str) -> str:
    '''Translate a word or a sentence to pig latin
    
    :param text: Word or sentence to be translated
    :type text: str
    '''
    words = text.split()
    translated_words = []

    for word in words:
        if word.startswith('xr') or word.startswith('yt') or word[0] in 'aeiou':
            translated_words.append(word + 'ay')
            continue 

        if word.startswith('y'):
            for index, letter in enumerate(word):
                if letter == 'y':
                    translated_words.append(word[index + 1:] + word[:index + 1] + 'ay')
                    break 
            continue 

        count = 0
        qu_found = False
        while count < len(word) and word[count] not in 'aeiou' and word[count] != 'y':
            if word[count:].lower().startswith('qu'):
                split_index = count + 2
                translated_words.append(word[split_index:] + word[:split_index] + 'ay')
                qu_found = True
                break
            count += 1
        
        if qu_found:
            continue

        count = 0
        y_found = False
        while count < len(word) and word[count] not in 'aeiou':
            if word[count] == 'y':
                translated_words.append(word[count:] + word[:count] + 'ay')
                y_found = True
                break
            count += 1
            
        if y_found:
            continue

        translated_words.append(word[count:] + word[:count] + 'ay')

    return " ".join(translated_words)



        