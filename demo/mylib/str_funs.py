TITLE = 'Srikanth Technologies'


def count_upper(st: str) -> int:
    """
    Count number of uppercase letters in the given string.
    :param st: Input string
    :return: Count of uppercase letters
    """
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


def hasspace(st: str) -> bool:
    """
    Checks whether string has a space
    :param st: Input string
    :return: True if string has a space otherwise False
    """
    return st.find(' ') >= 0


# Test - not to be executed when module is imported
if __name__ == '__main__':
    print(count_upper(TITLE))
    print(hasspace('xyz'))
