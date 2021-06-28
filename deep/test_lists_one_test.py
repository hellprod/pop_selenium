import pytest
from deep.list_to_lists import one_list_to_many_list

test_1 = {
    "test_input": [1, 2, 8, 3, 2, 4],
    "expected": [[1, 2, 8], [3], [2, 4]]
}

test_2 = {
    "test_input": [2,1,3,2],
    "expected": [[2], [1,3], [2]]
}

test_3 = {
    "test_input": [1,2,5,11,24,7,12,1,50,51,2,3],
    "expected": [[1,2,5,11,24], [7,12], [1,50,51], [2,3]]
}

test_4 = {
    "test_input": [1,2,3,1,2,33,1,2,2,2,2,3,3,3,2,2,3,2,4,6,8,234,432423,4234,2,3424,234,234234,423423,234234,134],
    "expected": [[1, 2, 3], [1, 2, 33], [1, 2], [2], [2], [2, 3], [3], [3], [2], [2, 3], [2, 4, 6, 8, 234, 432423], [4234], [2, 3424], [234, 234234, 423423], [234234], [134]]
}


@pytest.mark.parametrize("test_input,expected", [(test_4["test_input"], test_4["expected"]), (test_3["test_input"], test_3["expected"]), (test_2["test_input"], test_2["expected"]), (test_1["test_input"], test_1["expected"])])
def test_list_one( test_input, expected):
    assert one_list_to_many_list(test_input) ==  expected




