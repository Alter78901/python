'''
answer=input("请问您喝酒了吗？")
if answer=='y':
    proof=eval(input('请输入酒精含量：\n'))
    if proof<20:
        print('构不成酒驾,祝您一路平安')
    elif proof<80:
        print('已构成酒驾，请不要开车')
    else:
        print('已达到醉驾标准，请千万不要开车')
else:
    print('你走吧，没你啥事！')

user_name=input('请输入您的用户名：\n')
pwd=input('请输入您的密码：\n')
if user_name=='zs' and pwd=='123':
    print('登录成功')
else:
    print('用户名或密码不正确')

num = 0
for i in 'Hello':
    num+=1
    num+=1
    num+=1
    print(num,i)

for i in range(1,9999):

    if i % 3 == 0:
        print(i,'是3的倍数')
    # else:
    #     print(i,'是奇数')
answer = input('今天要上课吗? y/n:')
while answer == 'y':
    print('好好学习，天天向上')
    answer = input('今天要上课吗? y/n:')
'''
y = 0
i = 1
while i <= 100:
    y += i
    i += 1
else:
    print('1~100之间累加的和：', y)
