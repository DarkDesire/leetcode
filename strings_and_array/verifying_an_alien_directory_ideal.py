'''
time O(M)  m total # of chars in the list
space O(1) keys are at maz 26(lower alphachars)
'''
from typing import *

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        
        order_map = dict()
        
        for idx, char in enumerate(order):
            order_map[char] = idx
        
        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]
            
            # case when words are INVALID like ("apple", "app")
            if len(first_word) > len(second_word) and first_word.startswith(second_word):
                return False
            
            # loop thru chars to check when they are not equal and order is right
            for idx in range(len(first_word)):
                if first_word[idx] != second_word[idx]:
                    # check if order is not right
                    if order_map[first_word[idx]] > order_map[second_word[idx]]:
                        return False
                    
                    break # exit this loop since the first != should be the only thing to compare
        
    
        return True