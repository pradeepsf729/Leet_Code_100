# find if the array has duplicate item.

import pytest

"""
Time  : O(n)
Space : O(n)
"""
def find_dup(items):
    d = {}
    for i in items:
        if i in d:
            return True
        else:
            d[i] = 0
    return False


"""
Time  : O(nlogn)
Space : O(1)
"""
def find_dup_1(items):
    try:
        items.sort()
    except TypeError as e:
        return False # different types.
    cur_item = None
    for i in items:
        if not cur_item:
            cur_item = i
        else:
            try:
                if i == cur_item:
                    return True
                else:
                    cur_item = i
            except TypeError as e:
                return False # different types.
    return False

# Testing
# >pytest <file name>

"""
test_cases = [
    # Duplicates
    ([1, 2, 3, 1], True),
    ([5, 5, 5, 5, 5], True),
    ([10, 20, 30, 10, 40], True),
    (["apple", "banana", "apple"], True),
    ([1, 1.0], True),  # 1 == 1.0 in Python

    # No duplicates
    ([], False),
    ([42], False),
    ([1, 2, 3, 4, 5], False),
    ([1, "1", 1.00001], False),
]

@pytest.mark.parametrize("input_array, expected", test_cases)
def test_fn_dup(input_array, expected):
    result = find_dup(input_array)
    assert result == expected, f"Failed for input: {input_array}. Expected: {expected}, Got: {result}"


# Performance tests
def test_large_input_no_duplicates():
    input_array = list(range(10_000_000))
    assert find_dup(input_array) is False


def test_large_input_with_duplicate():
    input_array = list(range(10_000_000)) + [1]
    assert find_dup(input_array) is True

test_cases = [
    # Duplicates
    ([1, 2, 3, 1], True),
    ([5, 5, 5, 5, 5], True),
    ([10, 20, 30, 10, 40], True),
    (["apple", "banana", "apple"], True),
    ([1, 1.0], True),  # 1 == 1.0 in Python

    # No duplicates
    ([], False),
    ([42], False),
    ([1, 2, 3, 4, 5], False),
    ([1, "1", 1.00001], False),
]

@pytest.mark.parametrize("input_array, expected", test_cases)
def test_fn_dup_1(input_array, expected):
    result = find_dup_1(input_array)
    assert result == expected, f"Failed for input: {input_array}. Expected: {expected}, Got: {result}"


# Performance tests
def test_large_input_no_duplicates_1():
    input_array = list(range(10_000_000))
    assert find_dup_1(input_array) is False


def test_large_input_with_duplicate_1():
    input_array = list(range(10_000_000)) + [1]
    assert find_dup_1(input_array) is True

"""
