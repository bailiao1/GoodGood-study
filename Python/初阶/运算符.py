# 算术运算符：+ - * / // % **
print(1 + 1)                                                    # 1 + 1 = 2 不用多说吧？
print(1 + 1.0)                                                  # 2.0 只要对象中有一个浮点类型，那么结果也一定会是浮点型

print(3 - 1)                                                    # 2
print(1 * 2)                                                    # *:乘法 1 * 2 = 2

print(4 / 2)                                                    # /:除法 4/2 = 2.0 自动创建浮点型了
print(5 / 2)                                                    # 2.5

print(5 // 2)                                                   # //:取整数 5 // 2 = 2 余数直接丢掉
print(5 % 2)                                                    # %: 取模(5 - (2 * 2) = 1) 5 % 2 = 1

print(2 ** 3)                                                   # **：幂(次方)
                                                                # 2^3 = 8


# 关系运算符：== != > < >= <= (比较大小)
print(2 == 2)                                                   # True ( ==是判断值，=是赋值，is是判断引用是否为同一个对象)
print(2 != 3)                                                   # True
print(3 > 2)                                                    # True
print(2 >= 2)                                                   # True
print(2 <= 3)                                                   # True
print(2 <= 2)                                                   # True



# 逻辑运算符：

# and: 连接多个判断，它们必须全部成立(为真). 只要一个判断的结果为False(假)，输出就是False
print( 3>2 and 2<3)                                               # True (and)
# and 会返回第一个为 False 的值，或者最后一个值：
print(1 and 2)                                                    # 2 (两个都为真，返回最后一个)
print(0 and 2)                                                    # 0 (0为假，直接返回0)
print("" and 123,end='.')                                         # 空(空的字符串为假,直接返回。没错，单纯的空，没有占位，end直接顶到第一格)


# or：连接多个判断，只要其中之一成立，就是True
print(3<2 or 2>1)                                                   # True
# or会返回第一个为True的值,或者最后一个值：
print(0 or 2)                                                       # 2
print(0 or [])                                                      # []


# not: 对布尔值取反，False为True，True为False
print(not False)                                                    # True ()
# not只是对布尔值取反，不是!= 无法作为中间词判断，只能做前缀


# 逻辑运算优先级(not > and > or)
print(True or False and not False)                                 # True
# not False == Ture , False and Ture == False , True or False == True




# is：比较两个对象的地址（引用），即是否指向同一块内存。
a = 1
b = 2
print(a is b)                                                      # False
b = a                                                              # 此时将a赋值b
print(a is b)                                                      # True
a = 3                                                              # 修改a
print(b,a is b)                                                    # 1 False (b没有被影响,它们再次分离)

c = a-2
print(b is c)                                                      # True (python的缓存优化机制，数值重复利用，2的引用被再次分配)
                                                                   # 但这时肯定要问了：主播主播，在这样的背景机制下，is能不能作为 == 呢？

a = [1,2]                                                          # 但缓存机制不可能全给你存了(默认只会缓存-5 to 256之间的整数,还有部分场景的一些简单的字符串)
b = [1,2]                                                          # is判断的还是引用，而非它们的数值
print(a is not b)                                                  # True (此刻ab被分别创建，且各自分配了一块内存)，is需要修饰在not前


# in：判断某某中是否包含某某
a = [1,2,3]
b = "Hello"

print(1 in a)                                                       # True
print("W" not in a)                                                 # True
