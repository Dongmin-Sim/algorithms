'''
문제 : 유효한 펠린드롬
출처 : 리트코드
'''
import collections
from typing import Deque
import re


def use_list(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    # 펠린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

    

def use_list2(self, s: str) -> bool:
    strs = s.replace(' ', '')
    strs = list(map(lambda s:s.lower(), strs))

    # 펠린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def use_deque(self, s:str) -> bool:
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 펠린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def use_slicing(self, s:str) -> bool:
    s = s.lower()

    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    
    return s == s[::-1]


if __name__ == "__main__":
    string = input()
    
    print(use_list(string))
    print(use_list2(string))
    print(use_deque(string))
    print(use_slicing(string))