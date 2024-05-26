# def hs(z,x,y):
#     if(y >= 37.5):
#         print(f'{x}，您的体温大于37.5，需要隔离，隔离方式是{z}')
#     else:
#         print(f'{x}，您的体温小于37.5，体温正常')
#
# x=input('请输入您的姓名')
# y=eval(input('请输入您的体温'))
# z=input('请输入您的隔离方式')
# hs('居家隔离',x,y)

# def hs(x,y,z='居家隔离'):
#     if(y >= 37.5):
#         print(f'{x}，您的体温大于37.5，需要隔离，隔离方式是{z}')
#     else:
#         print(f'{x}，您的体温小于37.5，体温正常')
#
# x=input('请输入您的姓名')
# y=eval(input('请输入您的体温'))
# z=input('请输入您的隔离方式')
# hs(x,y)

def add(a,b):
    result =a+b
    return result

r= add(1,2)
print(r)
