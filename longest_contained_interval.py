from typing import List,Dict

from test_framework import generic_test

"""
    Take in a set of integers represented by an array, and return the size of a largest subset of integers
    in the array having the properties that if two integers are in the subset, then so are all integers
    between them.

    Subset, order doesn't matter
    Sets are unordered
    AKA Longest increasing range

    Input = [3,-2,7,9,8,1,2,0,-1,5,8]
    Sorted Input = [-2,-1,0,1,2,3,5,7,8,8,9]
    Largest subset = [-2,-1,0,1,2,3]
    Returns 6

    Brute force:
    - sort array in ascending order
    - find largest increasing sequence
    - return the length
    - Time: O(nlogn) + O(n) = O(nlogn)
    - Space: Constant O(1)

    Alternate approach for linear time or better:
    - dict: {3:False, -2:False, 7:False, 9:False, 8:False, 1:False, 2:True, 0:False, False:False, 5:False, 8:False}
    - [-2,-1,0,1,2,3,5,6,7,8,9,10,11,12,13,14,15]
    - dict
    - process again
    - lowest: 7
    - highest: 7
    - maxRange: 3+2+1=6
    - see if range
        - visit: set dict[element]=True
        - higher: update highest 
        - lower: update lowest, compute maxRange = max(maxRange,highest-lowest+1)
    - next element
        - skip if dict[element]==True
        - if False, then do above process again

"""
def findRangeOfNum(num:int, ht:Dict[int,bool]) -> int:
    highest = lowest = num
    while highest + 1 in ht:
        highest += 1
        ht[highest] = True
    while lowest - 1 in ht:
        lowest -= 1
        ht[lowest] = True
    return highest - lowest + 1

def longest_contained_range(A: List[int]) -> int:
    # TODO - you fill in here.

    # Create the hash table
    ht = {n:False for n in A}

    # Loop through A
    maxRange = 0
    for num in A:
        # Process if unprocessed
        if not ht[num]:
            maxRange = max(maxRange,findRangeOfNum(num,ht))

    # Return
    return maxRange


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
