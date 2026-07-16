def count_upper(st):
    """
    Count the number of uppercase characters in a string.

    Args:
        st (str): The input string to count uppercase characters from.

    Returns:
        int: The number of uppercase characters found in the string.

    Example:
        >>> count_upper('How Are You')
        3
        >>> count_upper('hello')
        0
        >>> count_upper('PYTHON')
        6
    """
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count




print(count_upper('How Are You'))




print(count_upper('How Are You'))

