import pytest
from calculator import calculate_average, is_passing, get_grade_category


def test_calculate_average():
    assert calculate_average([10, 12, 14]) == 12


def test_is_passing():
    assert is_passing(12) is True
    assert is_passing(8) is False


def test_empty_grades():
    with pytest.raises(ValueError):
        calculate_average([])


def test_grade_categories():
    assert get_grade_category(17) == "Excellent"
    assert get_grade_category(13) == "Good"
    assert get_grade_category(10.5) == "Average"
    assert get_grade_category(7) == "Fail"


def test_passing_grade_is_exactly_ten():
    assert is_passing(10) is True
