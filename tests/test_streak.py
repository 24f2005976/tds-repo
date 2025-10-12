import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

@pytest.mark.parametrize("nums,expected", [
    ([1, 1, 1], 3),                     # all positive
    ([2, 3, -1, 5, 6, 7, 0, 4], 3),     # example in brief (longest is 5,6,7 -> length 3)
    ([0, 0, 0], 0),                     # all zeros break streaks
    ([-1, -2, -3], 0),                  # all negatives
    ([1, 2, 0, 3, 4, 5, -1, 6, 7], 3),  # multiple streaks, middle is longest
    ([5], 1),                           # single positive
    ([0], 0),                           # single zero
    ([-1], 0),                          # single negative
])
def test_various_streaks(nums, expected):
    assert longest_positive_streak(nums) == expected

def test_multiple_equal_longest():
    # multiple runs of same longest length -> still returns that length
    nums = [1,1,0,2,2,0,3,3]
    assert longest_positive_streak(nums) == 2

def test_long_run_then_break():
    nums = [1,2,3,4,5,0,1,2]
    assert longest_positive_streak(nums) == 5
