'''
A leap year (in the Gregorian calendar) occurs:

In every year that is evenly divisible by 4.
Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
'''

def leap_year(year: int) -> bool:
    '''Checks if a year is a leap year. Returns True if the year is a leap year
    
    :param year: Year to be checked
    :type year: int
    '''
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        return True

    return False

print(leap_year(1996))