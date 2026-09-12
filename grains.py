'''
Calculate the number of grains of wheat on a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.

Write code that calculates:

the number of grains on a given square
the total number of grains on the chessboard
'''


def square(number: int) -> int:
    '''
    Calculates the number of grains in each square of the chessboard. 
    
    :param number: Index of the chessboard square.
    :type number: int
    '''
    count = 0 
    if 1 <= number <= 64:
        for num in range(number):
            count = 2 ** num
        return count
    raise ValueError('square must be between 1 and 64')


def total() -> int:
    '''
    Calculates the total number of grains on the chessboard
    '''
    grains = 0
    for num in range(64):
        grains += 2 ** num
    return grains