class Solution:
    def isValid(self, s: str) -> bool:
        char = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for i in range(len(s)):
            # if s not in char, append s to stack list
            if s[i] not in char:
                stack.append(s[i])
            # if stack is empty or char[s] is not equal to last stack value, return False
            elif not stack or char[s[i]] != stack.pop():
                return False
        
        # if there are no elements in the stack, return True
        return len(stack) == 0