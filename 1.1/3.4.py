def lengthOfLongestSubstring(s):
    if not s:
        return 0

    start = 0  # 滑动窗口的起始位置
    max_length = 0  # 最长无重复字符子串的长度
    char_set = set()  # 用于存储当前窗口中的字符

    for end in range(len(s)):
        # 如果当前字符不在窗口中，则添加到窗口中
        while s[end] in char_set:
            # 如果当前字符在窗口中，则移动窗口的起始位置，并从窗口中移除该字符
            char_set.remove(s[start])
            start += 1

            # 添加新字符到窗口
        char_set.add(s[end])
        # 更新最长无重复字符子串的长度
        max_length = max(max_length, end - start + 1)

    return max_length


# 示例用法
s = 'kj'
print(lengthOfLongestSubstring(s))  # 输出：3，最长无重复字符子串为 "abc"