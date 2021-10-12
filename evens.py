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
        if numbers == []:
            return False
    else:
        raise TypeError("A list was not passed into the function")


if __name__ == '__main__':
    print(even_of_evens(5))
