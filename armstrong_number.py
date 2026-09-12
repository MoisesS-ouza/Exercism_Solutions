'''An Armstrong number is a number that is the sum of its own digits each 
raised to the power of the number of digits.
Ex: 153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 '''

def is_armstrong_number(number: int) -> bool:
    '''Checks if a number is an armstrong number
    
    :param number: number to be checked
    :type number: int
    '''
    num_sum = 0
    num_digits = len(str(number))
    for digit in str(number):
        num_sum += int(digit) ** num_digits

    if num_sum == number:
        return True

    return False

print(is_armstrong_number(154))