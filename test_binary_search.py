import pytest

# IMPORTANTE: esta función aún no existe (la hará dev_2)
from searching import binary_search


def test_binary_search_found_middle():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2


def test_binary_search_not_found():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 10) == -1


def test_binary_search_empty_list():
    arr = []
    assert binary_search(arr, 1) == -1


def test_binary_search_first_element():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 1) == 0


def test_binary_search_last_element():
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 9) == 4