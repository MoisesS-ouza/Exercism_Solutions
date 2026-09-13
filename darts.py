'''
Created a dart game based on circle radius formula:
First you need to calculate the cartesian formula for
a cricle centered at the origin: x² + y² = C
After that, you have to calculate the radius, which is basically sqrt(C)
- the square root of the circle formula.
'''

from math import sqrt
def score(x: int, y:int) -> int:
    '''Determines your score based on the coordinates you chose
    
    :param x: the horizontal coordinates
    :param y: the vertical coordinates
    :type x: int
    :type y: int
    '''
    formula_circle = x ** 2 + y ** 2
    radius = sqrt(formula_circle)

    if radius > 10:
        return 0
    if 5 < radius <= 10:
        return 1
    if radius > 1:
        return 5

    return 10

print(score(1, 1))