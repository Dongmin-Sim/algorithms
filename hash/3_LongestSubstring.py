class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        
        for index, char in enumerate(s):
            # 새로운 값이 이전에 본 값이면서 현재 window 안에 존재하는 값으로 중복일때
            if char in used and start <= used[char]:
                # 현재 window에서 중복인 값보다 하나 앞으로 
                start = used[char] + 1
            # 한번도 보지 못했거나, 봤더라도 현재 윈도우에 없다면 max_length 계산
            else:
                max_length = max(max_length, index - start + 1)
                
            used[char] = index
            
        return max_length
