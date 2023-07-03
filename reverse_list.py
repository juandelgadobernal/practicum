#! /usr/bin/env python
"""Write a function that takes an array as input and returns the array in reverse order."""


def reverse(list_original):
    """
    Function that takes an array as input and returns the array in reverse order.
    :param list_original:
    :return: list_reverse
    """

    list_reverse = []
    for x in list_original:
        list_reverse = [x] + list_reverse
    print(list_reverse)
    return list_reverse


if __name__ == '__main__':

    assert(reverse(["a", "b", "c", "d", "e"])) == ["e", "d", "c", "b", "a"], "Positive scenario"
    assert(reverse([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1], "Positive scenario"
    assert(reverse([1, "mike", "Jhon", "c123z", 5])) == [5, "c123z", "Jhon", "mike", 1], "Positive scenario"
    assert(reverse(["a", "b", "c", "d", "e"])) != ["e", "d", "c", "b"], "Negative scenario - length"
    assert(reverse(["a", "b", "c", "d", "e"])) != ["e", "d", "c", "b", "x"], "Negative scenario - not match"
