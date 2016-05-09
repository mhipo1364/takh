__author__ = 'moefar'


def is_divisible(x, y):
    """
    Check if x is divided by y
    :param x: int
    :param y: int
    :return: bool
    """
    if x % y == 0:
            return True


def divisible_by_three(x):
    """
    Returns proper string if x is divided by 3
    :param x: int
    :return: str/None
    """
    if is_divisible(x, 3):
        if is_divisible(x, 5):
            return '{} Big Bang \n'.format(x)
        return '{} Big \n'.format(x)


def divisible_by_five(x):
    """
    Returns proper string if x is divided by 5
    :param x: int
    :return: str/None
    """
    if is_divisible(x, 5):
        if is_divisible(x, 3):
            return '{} Big Bang \n'.format(x)
        return '{} Bang \n'.format(x)


def main(x):
    """
    Decision Maker
    :param x: int
    :return: str/None
    """
    result = divisible_by_three(x)
    if not result:
        result = divisible_by_five(x)
    return result


start = 4
end = 146

for i in range(start, end):
    print(main(i))
