from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 중첩함수: 함수 안의 함수로 부모 함수의 변수를 자유롭게 사용할 수 있다.
            # 이 경우에는 매번 grid를 넘겨주지 않아도 된다는 것과 dfs함수를 self를 통해 불러오지 않아도 된다는 장점을 가짐
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
                
            grid[i][j] = '0'
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
                    
        return count