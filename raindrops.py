'''
Raindrops is a slightly more complex version of the FizzBuzz challenge, 
a classic interview question.
'''

def convert(number: int) -> str:
    '''Convert a number into its corresponding raindrop sounds
    
    :param number: number to be checked
    :type number: int
    '''
    string = ''
    if number % 3 == 0:
        string += 'Pling'
    if number % 5 == 0:
        string += 'Plang'
    if number % 7 == 0:
        string += 'Plong'

    if string == '':
        return str(number)
    return string 
