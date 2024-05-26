'''
i=0
while i < 3:
    user_name=input('请输入您的用户名：\n')
    pwd=input('请输入您的密码：\n')
    if user_name=='zs' and pwd=='123':
        print('系统正在登陆，请稍后')
        i=4
    else:
        if i < 2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
        i+=1
if i==3:
    print('对不起，3次输入错误')


for i in range(0, 3):
    for j in range(0, 4):
        print('*', end='')
    print()
print('---------------------------')


for i in range(1, 6):
    print('*' * i)


i=5
while i > 0:
    print('*' * i)
    i-=1
print('-'*40)

for i in range(1,6):
    print(' '*(5-i) + '*' * (2 * i - 1)+' '*(4-i))

print('-' * 40)
for i in range(1, 5):
    print(' ' * (4 - i) + '*' * (2 * i - 1) + ' ' * (4 - i))
for i in range(1, 4):
    print(' ' * i + '*' * (2 * (4 - i) - 1) + ' ' *i)


n = 3
for i in range(1, n + 1):
    for j in range(1, (n + i - 1) + 1):
        if j == n + 1 - i or j == n - 1 + i:
            print('*', end='')
        else:
            print(" ", end='')
    print('')
for i in range(1, n):
    for j in range(1, (2 * n - 1 - i) + 1):
        if j == i + 1 or j == 2 * n - 1 - i:
            print('*', end='')
        else:
            print(" ", end='')
    print('')


for i in 'hello':
    if i == 'o':
        break
    print(i)

s=0
i=1
while i<=100:
    if i % 2 ==1:
        i+=1
        continue
    s+=i
    i+=1

print('1-100之间的偶数和：',s)
'''
# while True:
#     print('你好')
#     pass
for i in range(8):
    if i % 2 !=1:

        continue
    else:
        print(i,end=',')