nums = list(input())
nums.sort()
sym = ['+','*']

expression = ''

i = 0
num_zero = 0
while True:
    if i >= len(nums):
        break
    elif sum(nums) == 0:
        expression = 0

    if nums[i] == '0':
        num_zero += 1
        i += 1
    else:
        temp = sum(nums[0:num_zero])


    if nums[i] == '0':
        expression = '(' + nums[i] + sym[0]+  nums[i+1] + ')' + sym[1]
        i += 2
    else:
        pass


print(eval(expression))
