import pytest

# IMPORTANTE: esta función aún no existe (la hará dev_2)
from searching import linear_search


def test_linear_search_found_middle():
    arr = [1, 3, 5, 7, 9]
    assert linear_search(arr, 5) == 2


def test_linear_search_not_found():
    arr = [1, 3, 5, 7, 9]
    assert linear_search(arr, 10) == -1


def test_linear_search_empty_list():
    arr = []
    assert linear_search(arr, 1) == -1


def test_linear_search_first_element():
    arr = [4, 2, 6, 8]
    assert linear_search(arr, 4) == 0


def test_linear_search_last_element():
    arr = [4, 2, 6, 8]
    assert linear_search(arr, 8) == 3