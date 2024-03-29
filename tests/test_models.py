"""Tests for statistics functions within the Model layer."""
import pytest
import numpy as np
import numpy.testing as npt
from inflammation.models import daily_mean
from inflammation.models import daily_max
from inflammation.models import daily_min
    
def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

def test_daily_max():
    """Test that max function works for an array of positive integers."""
    test_input = np.array([[4, 2, 5],
                           [1, 6, 2],
                           [4, 1, 9]])
    test_result = np.array([4, 6, 9])

    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_min():
    """Test that min function works for an array of positive and negative integers."""
    test_input = np.array([[ 4, -2, 5],
                           [ 1, -6, 2],
                           [-4, -1, 9]])
    test_result = np.array([-4, -6, 2])

    npt.assert_array_equal(daily_min(test_input), test_result)

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    #from inflammation.models import daily_min
    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])    



@pytest.mark.parametrize(
    "test_input, test_result",
    [
        ([[1,2],[1,3]],[1,2]),
        ([[0,3],[1,5],[6,2]],[0,2]),
    ])

def test_daily_min2(test_input, test_result):
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test_input)),np.array(test_result))
        
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))        
