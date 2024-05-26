# number=eval(input('请输入您的六位中奖号码：\n'))
# if number==123456:
#     print('恭喜你您中奖了')
# else:
#     print('您未中奖')
# print("------以if判断的表达式，是通过比较运算符计算出来的，结果是布尔值")
# n=98
# # if n % 2:
# #     print(n,'是奇数')
# if not n%2:
#     print(n,'为偶数')
#
# print('------------判断一个字符是否为空字符串---------------')
# x=input('请输入一个字符串')
# if x:
#     print('x是一个非空字符串')
# if not x:
#     print('x是一个空字符串')
#
"""
print('------------表达式也可以是一个单纯的布尔型变量------------')
flag=eval(input('请输入一个布尔型的值：True或False\n'))
if flag:
    print('flag的值为True')

if not flag:
    print('flag的值为False')
"""
'''
print('--------使用if语句是如果语句中只有一句代码----------')
a=10
b=7
if a>b:max=a
print('最大值为',max)
'''
score=eval(input('请输入您的成绩：\n'))
if score<0 or score>100:
    print('输入成绩有误')
elif 0<= score < 60:
    print('E')
elif 60<= score < 70:
    print('D')
elif 70<= score < 80:
    print('C')
elif 80<= score < 90:
    print('B')
else:
    print('A')
