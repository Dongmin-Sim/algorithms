from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(depth, string):
            if len(string) == len(digits):
                result.append(string)
                return 
            
            for i in range(depth, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, string + j)

        
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        dfs(0, '')
        
        return result