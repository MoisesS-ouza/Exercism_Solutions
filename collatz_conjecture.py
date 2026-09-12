'''
The Collatz conjecture is a famous unsolved math problem 
that asks if repeating two simple rules will always bring 
any positive whole number down to 1.

Rules:
If the number is even, divide it by 2
If the number is odd, multiply it by 3 and add 1
'''

def steps(number: int) -> int:
    '''Tells you how many steps for a number to reach 1, based on the
    Collatz conjecture
    
    :param number: Number to be checked
    :type number: int
    '''

    count = 0
    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            count += 1
        else:
            number = number * 3 + 1
            count += 1

    return count

print(steps(12))