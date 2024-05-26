def removeDuplicates(nums):
    if not nums:
        return 0

    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


# 示例
nums = [1, 1, 2]
result = removeDuplicates(nums)
print(nums[:result])  # 输出: [1, 2]
print(result)  # 输出: 2