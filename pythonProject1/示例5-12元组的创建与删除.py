#使用小括号创建元组
t=('hello',[10,20,30],'puthon','word')
print(t)

#使用内置函数tuple（）创建元组
t=tuple('helloword')
print(t)

t=tuple([10,20,30,40])
print(t)


print('10在元组中是否存在：',(10 in t))
print('10在元组中是不存在：',(10 not in t))
print('最大值',max(t))
print('最小值',min(t))
print('len:',len(t))
print('t.index:',t.index(10))
print('t.count',t.count(10))

t=('python','hello','word')

print(t[0])
t2=t[0:3:2]
print(t2)

for item in t:
        print(item)

for i in range(len(t)):
    print(i,t[i])

for index,item in enumerate(t):
    print(index,'---->',item)

for index,item in enumerate(t,start=11):
    print(index,'---->',item)

d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)

lst1={10,20,30,40}
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj)



d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
print({t:10})

print('max',max(d))
print('min',min(d))
print('len',lenm(d))