from typing import *

# 120 / 120 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Memory Usage: 13.9 MB

class Solution:
    
    def _is_sorted(self, first, second, order_dict) -> bool:
        continue_seq = None
        for i in range(min(len(first), len(second))):
            order_asc = order_dict[second[i]] >= order_dict[first[i]]
            is_the_same = first[i] == second[i]
            #print(first[i], second[i], order_asc, f"same: {is_the_same}")

            if order_asc and continue_seq is None:
                if not is_the_same: return True
                continue_seq = is_the_same
            elif order_asc and continue_seq:
                continue_seq = is_the_same
            else:
                return False
            
        if len(second) < len(first) and second in first:
            return False
            
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i
        
        result = []
        for i in range(len(words)-1):
            result.append(self._is_sorted(words[i], words[i+1], order_dict))

        return all(result)
