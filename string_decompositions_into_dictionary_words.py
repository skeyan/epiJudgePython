from typing import List
from collections import Counter

from test_framework import generic_test

"""
    Take a string that is a sentence, and a set of strings that are words, 
    and find substrings of the sentence that are concatenations of all of the words in any order.
    Return the starting indices of substrings of the sentence of sentence strings which are concatenations of all the concatenations in the words array.
    Each string must appear exactly once, and their ordering is immaterial.
    Assume that the words in the array have equal length, and it's possible to have duplicates.

    s: "afoobar" --> [1]
    s: "barfoobara" --> [0,3]
    s: "barfoobar" --> [0,3]
    s: "fooabar" --> []
    s: "fooabarfoo" --> [4]
    s: "barfoothefoobarman"
    words: ["foo", "bar", "foo"]    
    expected: [0, 9]

    substringIndices = [] keep track of the substring indices

    Naive:
    - find all possible concatenations of the words array
    - ex: foobar, barfoo
    - find the indices of each of those substrings in the sentence
    - use while loop and python's find() method until index is out of bounds, for every concatenation 
    - Time: 
        n = # of words
        m = length of each word
        Python find() is O(n*m)
        Multiply by N, the length of the sentence to get O(N*n*m)
    - Worst Possible Input:
        s: "aaaaaaaaaaaaaaaaaaaa"
        w: [a,a,a,a,a]

    Alternate approach:
    - substringInd = []
    - startingInd = 3
    - numWordsFoundSoFar = 2
    - ht = {bar:True, foo:True}
    - if numWordsFoundSoFar == len(words), append the starting index to the array
        - startingInd
        - set first to false, decrease numWords by 1
        - add 1 to startingInd
        - append startingInd to substringInd
    - Time: add all words to a ht, then loop through each character in sentence = O(n) + O(N*n*m) = O(N*n*m)
    - Space: substringInd (N) + ht (n*m) = O(N) + O(n*m)

    O(N) * O(n) vs O(N*n) --> no diff
"""
# Helper function 
# n = # of words
# m = length of each word
def isValidSubstring(s: str, startingInd:int, n:int, m:int, ht:Counter) -> bool:
    # Keep track of where we're at
    idx = startingInd
    
    # While we're in bounds
    while idx < len(s): # O(n)
        # Get the m-letter word we're dealing with
        word = s[idx:idx+m] # O(m) each word is m-length
        if word in ht and ht[word] > 0: # still need to find it
            n -= 1 # keep track of how many words we need still
            ht[word] -= 1

            # If we found all words for the substring
            if n == 0:
                return True

            # Increment by m
            idx += m
        else:
            return False
    
    return False

# Time: O(N*n*m) 
def find_all_substrings(s: str, words: List[str]) -> List[int]:
    # TODO - you fill in here.

    # Base case
    if len(words) == 0 or len(s) == 0:
        return []

    # Initialize variables
    substringInd = []
    n = len(words) # length of the words array
    m = len(words[0]) # length of each word

    # Use a counter ht to keep track of substring foundness
    for startingInd in range(len(s)-m+1): # O(N) outer loop
        ht = Counter(words) # O(n) hash table
        if isValidSubstring(s,startingInd,n,m,ht): # O(n*m)
            substringInd.append(startingInd)

    # Return
    return substringInd


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
