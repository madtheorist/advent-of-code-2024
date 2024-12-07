import pytest
from src.day_1 import distance_between_lists, similarity_score

@pytest.fixture
def inputs():
    list1 = [3, 4, 2, 1, 3, 3]
    list2 = [4, 3, 5, 3, 9, 3]
    return list1, list2

def test_distance_between_lists(inputs):
    list1, list2 = inputs
    assert distance_between_lists(list1, list2) == 11

def test_similarity_score(inputs):
    list1, list2 = inputs
    assert similarity_score(list1, list2) == 31
    assert similarity_score(list2, list1) == 31