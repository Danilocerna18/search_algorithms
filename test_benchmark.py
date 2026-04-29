import pytest
from searching import linear_search, binary_search


# Lista de 100,000 elementos
large_list = list(range(100000))


target = -1



def test_benchmark_linear_search(benchmark):
    benchmark.pedantic(
        linear_search,
        args=(large_list, target),
        rounds=5,
        iterations=5
    )



def test_benchmark_binary_search(benchmark):
    benchmark.pedantic(
        binary_search,
        args=(large_list, target),
        rounds=5,
        iterations=5
    )