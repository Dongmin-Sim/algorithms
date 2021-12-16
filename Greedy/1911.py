'''
문제 : 흙길 보수하기
분류 : #greedy
'''
import sys, math

def solution(N:int, L:int, water:list) -> int:
    wood = 0
    wood_end_index = 0

    for start, end in water:
        # 널판지가 새로운 웅덩이 시작 지점을 포함하는 경우
        if start <= wood_end_index:
            start = wood_end_index + 1

            if end <= start:
                continue

        curent_wood = math.ceil((end - start) / L)
        wood += curent_wood
        wood_end_index = max(wood_end_index, start + curent_wood * L - 1)

    return wood


if __name__ == "__main__":    
    input = sys.stdin.readline
    
    N, L = map(int, input().split())

    water = [list(map(int, input().split())) for _ in range(N)]
    water.sort()

    print(solution(N, L, water))
