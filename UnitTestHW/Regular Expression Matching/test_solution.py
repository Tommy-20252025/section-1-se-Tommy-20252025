import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()
    
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["a", ".*.", True],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]

@pytest.mark.parametrize("s,p,fuck", testcases)
def test_isMatch(solution,s,p,fuck):
    assert solution.isMatch(s, p) == fuck


@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch() == True

