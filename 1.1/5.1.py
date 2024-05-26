'''
全局变量：作用域是指整个文件
局部变量：作用域是在上下文中醉经的一整块同样缩进的Python语句
'''
str1='helloword'
for i in str1:
    str2 = 'myname'
    print(i,str2)
    for j in str2:
        print(j)