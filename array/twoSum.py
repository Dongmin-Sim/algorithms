
def advanced_loop(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


def key(nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return nums.index(num), nums_map[target - num]


def search_in(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

    return 


def brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i +1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9


