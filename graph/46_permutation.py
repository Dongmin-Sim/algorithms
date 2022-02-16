from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []
        
        def dfs(elements):
            if len(prev_elements) == len(nums):
                result.append(prev_elements[:])
            
            for e in elements:
                next_e = elements[:]
                next_e.remove(e)
                
                prev_elements.append(e)
                dfs(next_e)
                prev_elements.pop()

        
        dfs(nums)
        
        return result