from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()  # 先对数组进行排序
    closest_sum = float('inf')  # 初始化最接近的和为正无穷大
    min_diff = float('inf')  # 初始化最小差距为正无穷大

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            diff = abs(current_sum - target)

            # 如果当前和与目标值的差距更小，则更新最接近的和与最小差距
            if diff < min_diff:
                min_diff = diff
                closest_sum = current_sum

                # 根据当前和与目标值的大小关系，移动指针
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # 如果找到精确匹配，则直接返回结果
                return target

    return closest_sum  # 返回最接近的和


# 示例用法
nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosest(nums, target))  # 输出: 2