'''
Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers.
perfect - A number that the sum of all its divisors is exactly the number itself
abundant - A number that the sum of all its divisors is greather than the number itself
deficient - A number that the sum of all its divisors is lower than the number itself
'''
def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')
    aliquot_sum = 0
    for num in range(1, number):
        if number % num == 0:
            aliquot_sum += num

    if number == aliquot_sum:
        return 'perfect'
    if number < aliquot_sum:
        return 'abundant'
    if number > aliquot_sum:
        return 'deficient'
