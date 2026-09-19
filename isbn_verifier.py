'''
The ISBN-10 verification process is used to validate book identification numbers. 
These normally contain dashes and look like: 3-598-21508-8
'''

def is_valid(isbn: str) -> bool:
    '''
    Checks if the ISBN-10 is valid. Returns True if so.

    :param isbn: isbn identification number
    :type isbn: str
    '''
    for number in isbn:
        if number.isalpha() and not number.lower() == 'x':
            return False

    isbn = [x for x in isbn if x.isdigit() or x.lower() == 'x']
    sum_numbers = 0
    multi = 10

    if isbn == []:
        return False

    if len(isbn) == 10 or isbn[-1].lower() == 'x':
        if 'X' in isbn and isbn[-1].lower() != 'x':
            return False
            
        for number in isbn:
            if number.lower() == 'x':
                number = '10'
            sum_numbers += int(number) * multi
            multi -= 1

        if sum_numbers % 11 == 0:
            return True

        return False
    return False

print(is_valid("3598P215088"))
