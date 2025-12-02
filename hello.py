
#name = input('please enter your name: ')
#print('hello,', name)
#print("1024*768=",1024*768)
# print absolute value of an integer:
#a = 100
#if a >= 0:
 #   print(a)
#else:
 #   print(-a)
#print('I\'m ok.')
#print('I\'m learning\nPython.')
#print('\\\n\\')


#age=float(input('age=' ))
#if age >= 18:
 #  print('adult')
#else:
 #   print('teenager')
#name = input('please enter your name: ')
#print('name=',name)
#b =1000
#print('Hi, %s, you have $%d.' % ('name', b))


#a=input('your height=')
#b=input('your weight=')
#x=float(a)
#y=float(b)
#c=y/(x**2)
#print('your BMI is', c)
#if c<18.5:
 #   print('过轻')
#elif c>=18.5 and c<25:
 #   print('正常')
#elif c>=25 and c<28:
 #   print('过重')
#elif c>=28 and c<32:
 #   print('肥胖')
#else:
 #   print('严重肥胖')

#age=float(input('age ='))
#match age:
   # case x if x < 10:
    #    print('< 10 years old:', x)
    #case 10:
     #   print('10 years old.')
    #case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
     #   print('11~18 years old.')
    #case 19:
     #   print('19 years old.')
    #case _:
     #   print('not sure.')

# 无限循环示例
#while True:
 #   print("这是一个死循环，按 Ctrl + C 可停止运行。")
 #   print("这是一个死循环，按 Ctrl + C 可停止运行。")

#def xx(age,location='bj'):
#    print(age)
#    print(location)
#    return
#a=input('a=')
#b=input('b=')
#xx(a,'tj')
#a=int(input('a='))
#b=input('b=')

#def mul(x, *y):
#    for i in y:
#        x = x*i
#    return x
#print(mul(a,n))

#def mul(*args):
#    result = 1
#    for num in args:
#        result *= num
#    return result
#nums = input("请输入一个或多个数字（用空格分隔）：")
#num_list = [float(n) for n in nums.split()] #nums.split() 是 Python 中字符串的一个方法，用于将字符串分割成列表,默认按空格分割
#product = mul(*num_list)
#print("这些数的乘积是：", product)

#汉诺塔问题
#def move(n, a, b, c):
#    if n == 1:
#        print(a, '-->', c)
#    else:
#        move(n - 1, a, c, b)  # 先将 n-1 个盘子从 A 移到 B（借助 C）
#        print(a, '-->', c)    # 再将最大盘从 A 移到 C
#        move(n - 1, b, a, c)  # 最后将 n-1 个盘子从 B 移到 C（借助 A）

#杨辉三角
def triangles():
    row = [1]           # 第一行
    while True:
        yield row       # 产出当前行
        # 根据当前行生成下一行
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
n = 0
results = []
for t in triangles():
    results.append(t)#t,i这些都只是虚的，指向循环的对象，可以换做任意的字母
    n = n + 1
    if n == 10:
        break
for t in results:
    print(t)










