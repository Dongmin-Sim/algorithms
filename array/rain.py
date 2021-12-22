def stack(height):
    stack = []
    volumn = 0

    for i in range(len(height)):
        print('i : ', i)
        while stack and height[i] > height[stack[-1]]:
            print('stack:', stack)
            print(height[i], height[stack[-1]])
            top = stack.pop()

            if not len(stack):
                break
            print('top: ', top)
            print('stack:', stack)
            distance = i - stack[-1] - 1
            water = min(height[i], height[stack[-1]]) - height[top]
            print('disatnch : ', distance, 'water : ', water)

            volumn += distance * water

        stack.append(i)
        print('---')
    return volumn

def solution(height):
    if not height:
        return 0 
    
    volumn = 0 
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if left_max <= right_max:
            volumn += left_max - height[left]
            left += 1
        else:
            volumn += right_max - height[right]
            right -= 1

    
    return volumn


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print(stack(height))

