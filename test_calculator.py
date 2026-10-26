import pytest
from calculator import calculate_average, is_passing


def test_calculate_average():
    assert calculate_average([10, 12, 14]) == 12


def test_is_passing():
    assert is_passing(12) is True
    assert is_passing(8) is False


def test_empty_grades():
    with pytest.raises(ValueError):
        calculate_average([])
