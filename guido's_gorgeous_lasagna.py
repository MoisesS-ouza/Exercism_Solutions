"""Functions used in preparing Guido's gorgeous lasagna.
 
Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum
 
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
def bake_time_remaining(minutes):
    """Calculates the bake time remaining.
 
    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.
 
    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
 
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - minutes

def preparation_time_in_minutes(number_of_layers):
    '''Calculates the total preparation time for the layers of the lasagna'''
    minutes_layers = 2 * number_of_layers
    return minutes_layers
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Total elapsed time doing the lasagna'''
    time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return time

