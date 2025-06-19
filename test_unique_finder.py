import pytest
from unique_finder import find_unique_element

def test_regular_case():
    assert find_unique_element([1, 2, 3, 2, 1]) == 3

def test_larger_input():
    assert find_unique_element([4, 1, 2, 1, 2, 4, 5]) == 5

def test_negative_numbers():
    assert find_unique_element([-1, -2, -2, -3, -1, -3, 0]) == 0

def test_single_element():
    assert find_unique_element([99]) == 99

def test_non_integer_element():
    with pytest.raises(ValueError):
        find_unique_element([1, 1, 'a'])

def test_even_length_input():
    with pytest.raises(ValueError):
        find_unique_element([1, 1, 2, 2])

def test_non_list_input():
    with pytest.raises(TypeError):
        find_unique_element("not a list")
