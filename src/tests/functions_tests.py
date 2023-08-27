from src.functions import find_max_min_value


def test_positive_path_max_min_value():
    assert find_max_min_value([5, 6, 3, 1, 2, 3, 4, 5, 1, 2, 5]) == (6, 1)