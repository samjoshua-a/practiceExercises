def find_max(nums: list) -> list:
    max_num = nums[0]
    for _ in nums:
        if max_num < _:
            max_num = _
    return max_num

result = find_max([-1, -2, -3, -4, -5])
print(result)