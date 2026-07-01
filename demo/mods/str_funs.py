TITLE = 'Srikanth Technologies'


def count_upper(st: str) -> int:
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


def hasspace(st: str) -> bool:
    return st.find(' ') >= 0


# Test - not to be executed when module is imported
if __name__ == '__main__':
    print(count_upper(TITLE))
    print(hasspace('xyz'))
