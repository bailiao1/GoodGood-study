# 定义变量：将数据赋值给变量名，变量是可变的(被覆盖)
# 变量命名：变量名由大小写字母、_ 和数字组成。但数字不能作为变量名开头:(1a = 1) 错误命名会报错，某些python自带的关键词也不行(is,if...)

num1 = "你"
num2 = "还好"
a = "吗"
total = num1 + num2 + a                                         # ‘+’ 拼接变量
print(total + "?")                                              # 你还好吗?

print(type(num1))                                               # type():查看目标类型
                                                                # <class 'str'> 字符串类型

# 变量可交互
a, b = 1, 2
a, b = b, a                                                     # a = 2 , b = 1 一行完成交换


# 噔噔，常用类型小课堂：
a = 1                                                           # int：整型
b = 1.0                                                         # float：浮点型
c = "1"                                                         # str：字符串
d = True                                                        # bool：布尔类型，True（非0）/ False（0）
                                                                # 注意：True/False 本质是 bool 类型，但也能当作 1 / 0 使用
                                                                # bool 是 int 的子类（True == 1 → True）

e = None                                                        # None：空（啥也没有），类型是 NoneType
                                                                # 注意：在 if 判断中，None 会被当作 False，但：
                                                                # False != None（两者类型不同，值也不同）

print(type(a),type(b),type(c),type(d),type(e))                  # <class 'int'> <class 'float'> <class 'str'> <class 'bool'> <class 'NoneType'>

# 所以捏，数据也可以是字符串，数值...


# 类型转换：将数据的类型强行转换
a = '1.1'
print(float(a))                                                 # 1.1 字符串的数字变成了浮点型
# print(int(a))                                                 # 但在直接强转int时报错了

b = float(a)
print(int(b))                                                   # 1 但是我们可以先用一个值接收浮点型，接着再强转整型
                                                                # float转int时，小数点直接截断，没有四舍五入

print(bool(a),bool(b),bool(0),bool(None))                       # True True False False 只要非0/None 转bool后就是True

# 小补充：
print(int(True),float(False),str(None),bool(''),bool(' '),bool([]))     # Ture/False默认就是1/0嘛
#        1          0.0        None     False     True     False        # 空字符串和空格位是不同的，空格位是有值的，为True


