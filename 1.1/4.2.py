def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

            # 如果没有找到，根据题目要求可以返回空数组或抛出异常
    return []


# 示例用法
numbers = [2, 7, 11, 15]
target = 9
result = twoSum(numbers, target)
print(result)  # 输出应该是 [1, 2]，因为 2 + 7 = 9




