import csv
from collections import Counter

# 打开CSV文件
with open('attack.csv', 'r', encoding='utf-8') as csvfile:
    # 创建CSV阅读器
    data = csv.reader(csvfile)
    # 使用Counter来统计IP地址的出现次数
    ip_counter = Counter()

    # 跳过列名（如果有）
    next(data)

    # 遍历CSV文件中的每一行
    for row in data:
        # 假设IP地址是每行的第一个元素
        ip = row[0].replace('ip: ', '')  # 移除可能存在的前缀
        # 更新IP地址的计数
        ip_counter[ip] += 1

# 按出现次数降序排序
sorted_ips = sorted(ip_counter.items(), key=lambda x: x[1], reverse=True)

# 输出IP地址及其出现次数.
for ip, count in sorted_ips:
    print (f"IP地址: {ip}, 出现次数: {count}")