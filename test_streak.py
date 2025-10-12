import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    assert longest_positive_streak([-1, -2, -3]) == 0

def test_all_positive_numbers():
    assert longest_positive_streak([1, 2, 3]) == 3

def test_mixed_numbers():
    assert longest_positive_streak([1, 2, -3, 4, 5, 6]) == 3

def test_streaks_at_beginning_and_end():
    assert longest_positive_streak([1, 2, 3, -4, 5]) == 3

def test_single_element_list():
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0