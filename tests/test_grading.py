import pytest
from grading import average, get_grade, is_honors, is_passed


# 1. Параметризованная проверка всех границ и диапазонов get_grade
@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "5"),
        (90, "5"),
        (89, "4"),
        (75, "4"),
        (74, "3"),
        (60, "3"),
        (59, "2"),
        (0, "2"),
    ],
)
def test_get_grade_boundaries(score, expected):
    assert get_grade(score) == expected


# 2. Строгая проверка исключений get_grade с точным совпадением текста (^...$)
def test_get_grade_invalid_scores():
    exact_pattern = r"^score must be between 0 and 100$"
    with pytest.raises(ValueError, match=exact_pattern):
        get_grade(-1)
    with pytest.raises(ValueError, match=exact_pattern):
        get_grade(101)


# 3. Полная проверка функции is_passed (порог по умолчанию 60 и явный порог)
def test_is_passed_default_threshold():
    assert is_passed(60) is True
    assert is_passed(59) is False


def test_is_passed_custom_threshold():
    assert is_passed(75, threshold=75) is True
    assert is_passed(74, threshold=75) is False


# 4. Проверка функции average
def test_average_valid():
    assert average([80, 90]) == 85.0
    assert average([100]) == 100.0


def test_average_empty():
    with pytest.raises(ValueError, match=r"^scores must not be empty$"):
        average([])


# 5. Дополнительное задание: проверка функции is_honors
def test_is_honors_boundaries():
    assert is_honors([90, 90]) is True
    assert is_honors([89, 90]) is False
    assert is_honors([100, 100]) is True
