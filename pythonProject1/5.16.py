d={1001:'李梅',1002:'王华',1003:'张锋'}
print(d)

d[1004]='张丽丽'
print(d)

keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

values=d.values()
print(values)
print(list(values))
print(tuple(values))

lst=list(d.items())
print(lst)

d=dict(lst)
print(d)

print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在'))

print(d.popitem())
print(d)

def get_sum(num):
    s=0
    for i in range(1,num+1):
        s+=i
        print(f'1到{num}之间的累加和为：{s}')

get_sum(10)
get_sum(100)
get_sum(1000)
