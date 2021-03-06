def even_of_evens(numbers):
    """
    Should raise TypeError if a list is not passed into the error message:
    "A list was not passed into the function"
    * If numbers is empty: return False
    * If the number of even numbers is odd, return False
    * If the number of even numbers is 0, return False
    * If the number of even numbers is even, return True
    """

    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])
        return bool(evens and evens % 2 == 0)
    raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    even_of_evens([5, 7, 9, 2, 18])
