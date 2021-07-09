from typing import List

from test_framework import generic_test

"""
    Return of length of longest subarray with property that all its elements are distinct
    Array = [f,[[s,f,e,t,w,]]e,n,w,e]
                 s           ^
    subArr = [s,f,e,t,w]

    subarray: contiguous
    subsequence: non-contiguous
    no duplicated letters in the subarray

    maxLength: keep track of the longest subarray we've seen so far
    seen: Dict - keep track of the last index we saw each letter
    currentStartInd: keep track of the start of our current subarray

    currentStartInd = 4
    maxLength = 5
    seen = {f:2, s:1, e:6, t:4, w:5, n:7}

    - keep track of current index
    - add/update seen
    - increase max length
        - maxLength = max(maxLength, index - currentStartInd + 1)
    - increase current start index when found duplicate that is >= currentStartInd
        - make it equal to the seen[duplicated element] + 1 
    
    ------
    Array = [44, 87, 87, 62, 96, 102, 44]
                     s                ^
    expected: 5
    maxLength = 2
    csi = 2
    seen = {44:0, 87:2, 62:3, 96: 4, 102: 5}
"""

def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    # TODO - you fill in here.
    maxLength = 0
    currentStartInd = 0
    seen = {}

    # Loop through the array of elements
    for i in range(len(A)):
        if not A[i] in seen or seen[A[i]] < currentStartInd:
            seen[A[i]] = i
            maxLength = max(maxLength, i - currentStartInd + 1)
        else:
            if seen[A[i]] >= currentStartInd:
                currentStartInd = seen[A[i]] + 1
                seen[A[i]] = i

    # Return
    return maxLength


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))