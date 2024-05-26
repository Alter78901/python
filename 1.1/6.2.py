# print('hello world','天气真好',sep='----',end='\t')
# print('打篮球')

#定义一个参数 默认参数是p2=2
# def f(p1,p2=2):
#     print(p1+p2)
#
# f(1)
# f(1,5)
# print('-'*50)
#
# def f(p1,p2):
#     print(p1 - p2)
# f(p1=5,p2=2)
print('-'*50)

def f(a,p2=2):
    #print(f(5,p2=3))
    print(f'{a} + {p2} = ', a + p2)
f(5,p2=3)