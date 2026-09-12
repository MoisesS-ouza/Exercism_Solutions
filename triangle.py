'''
Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths.
'''

def equilateral(sides: list[int]) -> bool:
    '''Determines if a triangle is equilateral (three sides of the same length). Returns True if it's equilateral.
    
    :param sides: list of the sides of the triangle
    :type sides: list[int]
    '''
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]

    if side_1 > 0 and side_2 > 0 and side_3 > 0:
        if (side_1 + side_2 >= side_3) and (side_2 + side_3 >= side_1) and (side_1 + side_3 >= side_2):
            if side_1 == side_2 == side_3:
                return True

            return False
        return False
    return False

def isosceles(sides: list[int]) -> bool:
    '''Determines if a triangle is isosceles (two sides of the same length). Returns True if it's isosceles.
        
        :param sides: list of the sides of the triangle
        :type sides: list[int]
    '''
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]

    if side_1 > 0 and side_2 > 0 and side_3 > 0:
        if (side_1 + side_2 >= side_3) and (side_2 + side_3 >= side_1) and (side_1 + side_3 >= side_2):
            if (side_1 == side_2) or (side_1 == side_3) or (side_2 == side_3):
                return True

            return False
        return False
    return False

def scalene(sides: list[int]) -> bool:
    '''Determines if a triangle is scalene (three sides of different lengths). Returns True if it's scalene.
        
        :param sides: list of the sides of the triangle
        :type sides: list[int]
    '''
    side_1 = sides[0]
    side_2 = sides[1]
    side_3 = sides[2]

    if side_1 > 0 and side_2 > 0 and side_3 > 0:
        if (side_1 + side_2 >= side_3) and (side_2 + side_3 >= side_1) and (side_1 + side_3 >= side_2):
            if (side_1 != side_2) and (side_2 != side_3) and (side_1 != side_3):
                return True

            return False
        return False
    return False
    
