# def sum(*nums):
#     #定义一个半两，来保存结果
#     result = 0
#     #遍历元组，并将元组中的数进行累加
#     for n in nums:
#         result+=n
#     print(result)
#
# sum(123,456,789,10,20,30,40)

# # 函数嵌套
# def func_b():
#     print('---2---')
#
# def func_a():
#     print('---1---')
#
#     func_b()
#
#     print('---3---')
#
# func_a()
# def fun1(x,y):
#     print('这是函数一')
#     sum=x+y
#     return sum
# def fun2():
#     print('这是函数二')
#     sum = fun1(2,3)
#     print(sum)
# fun2()
# def max(x,y):
#     return x if x>y else y
# def maxs(a,b,c,d):
#     res1=max(a,b)
#     res2 =max(res1,c)
#     res3 = max(res2, c)
#     return res3
# print(maxs(5,2,420,299))
#递归函数示例
# 定义一个名为factoria的函数
# def factoria(n):
#     if n == 1:
#         return  1#边界
#     else:
#         return n * factoria(n-1)#递归函数
#
# #测试
# num = 10
# result=factoria(num)
# print(f"{num}的的递归函数是{result}")
n=int(input())#输入任意n表示n天时，剩下一个桃子
def F(x):
    if x==1:
        return x
    else:
        return (F(x-1)+1)*2#递归函数

print(F(n))#输出递归值

