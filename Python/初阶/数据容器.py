# 列表 (List)
# 使用 [] 创建
a = [1,2.5,'3',[4,5]]                                  # 将一串数据保存到一个变量中
b = []                                                 # 列表可以为空
print(a)                                               # [1, 2.5, '3', [4]]   (列表里可以保存各种数据类型)
print(b)                                               # []

# 索引
print(a[3][0])                                          # 4 (取出第 4 个值中的第 1 个值)索引从0开始计算

# 切片(包前不包后)
print(a[0:3:2])                                         # [1, '3'] (取出下标 0 到下标 2 的值，步长为2)

# 添加元素
b.append("hello")                                       # 整体添加
print(b)                                                # ['hello']

b.extend("ld")                                          # 分散添加(仅限可迭代对象:字符串,列表......)
print(b)                                                # ['hello', 'l', 'd'] ("ld"字符串被拆分成一个个单独的字符)

b.insert(1,'wor')                        # 指定位置添加
print(b)                                                # ['hello', 'wor', 'l', 'd'] 在原本索引[1]的插入


# 移除元素
b.remove('wor')                                         # 根据元素移除
print(b)                                                # ['hello', 'l', 'd']

del b[2]                                                # 根据下标移除
print(b)                                                # ['hello', 'l']

c = b.pop(1)                                            # 移除指定小标并返回值,如未指定，默认移除末尾
print(f"b:{b} c:{c}")                                   # b:['hello'] c:l


# 排序
a = [3,2,1,5,6]

a.sort()                                                # .sort(reverse=False) 只能用于列表,原地排序不能直接 print，reverse为True表示降序(从大到小)，False为升序(从小到大)，默认为False
b = sorted(a)                                           # sorted(reverse=False) 同理，但不是原地，且所有可迭代对象都能用
print(a,b)                                              # [1, 2, 3, 5, 6] [1, 2, 3, 5, 6]

#-----------------------------------------------------------------------------------------------------------------


# 元组(tuple)
# 使用 () 创建,一旦创建就不可再更改,只能再次创建不同地址(引用)的对象
t = (1, 2, 3, [4,'5',2],2)

print(t[3][0])                                          # 4 同样可通过下标访问

print(t[1:3])                                           # (2, 3, [4, '5', 2], 2)  同样可以切片(包前不包后)

print(len(t))                                           # 查看元组中元素个数，这里是：5

print(f"元素2在此元组出现了:{t.count(2)}次")               # 统计某元素出现次数，内嵌套中的元素无法被直接访问
                                                        # 元素2在此元组出现了:2次

print(t.index(2))                                       #  1 返回某元素第一次出现的索引，找不到就报错。


#--------------------------------------------------------------------------------------------------------------------

# 字典(dict)
# 使用 {} 创建键值对，可变、键唯一(即键名不可重复)
d = {"name":"D","age":2,"families":26}
c = {"name":"D + 1","age":3,"families":26}

print(d)                                                  # {'name': 'D', 'age': 2, 'families': 26} 不可通过下标直接访问,但可以用键名

d["name"] = 'd'                                           # 值可修改
print(d["name"])                                          # d 可通过键名访问值

print(d.keys())                                           # keys()  :返回所有键名       dict_keys(['name', 'age', 'families'])
print(d.values())                                         # values():返回所有值         dict_values(['d', 2, 26])
print(d.items())                                          # items() :返回所有键值对     dict_items([('name', 'd'), ('age', 2), ('families', 26)])

print(d.get("age"))                                       # get()   :返回指定键的值，如果不存在则返回None，更安全               2

# 删除元素
a = d.pop("age")                                          # pop()   :同样能在字典使用，删除指定键，返回对应的值
print(a)                                                  # 2

a = d.popitem()                                           # popitem() 删除并返回最后一个键值对
print(a)                                                  # ('families', 26)

d.clear()                                                 # clear() 清空字典
print(d)                                                  # {}

d.setdefault("name","D")                                  # # setdefault(key, default): 获取键值对,若无则新增并设置默认值

d.update(c)                                               # update() 合并另一个字典
print(d)                                                  # {'name': 'D + 1', 'age': 3, 'families': 26} setdefault增加的同名键"name"被覆盖，键唯一

# 字典排序(sorted(x,key,reverse=False))
d = {"a": 3, "b": 1, "c": 2}

# 按值大小排序
sorted_items = sorted(d.items(), key=lambda x: x[1])      # 先获取d.items():由元组组成的列表,再自定义key(以什么为目标进行排序)，这里原地设置了一个匿名函数，用元组的索引获取各个值，再根据值进行排序。
print(sorted_items)                                       # [('b', 1), ('c', 2), ('a', 3)]

# 若要保留字典形式，则可以使用字典推导式(末尾细说)
sorted_dict = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
print(sorted_dict)                                        # {'b': 1, 'c': 2, 'a': 3}

# key只是自定义的规矩，还可以使用len()这些许多方法获取需要比较的值
# 键名只能使用可哈希对象，如str，int等

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 集合(set) 无序(但 python3.7后保留了插入顺序)，值唯一(可用于去重)，且值必须是可哈希的(即不可变)
# 使用 {} 创建

s = {2,1,(3,4),5}                                           # 元组不可变，所以可以加入集合。但当元组中包含可变对象，如列表等，集合就会报错。错误示例：s = {1,2,(3,[4]),5}
print(s)                                                    # {1, 2, 5, (3, 4)} 再次打印大概也是这个结果，因为插入顺序被保留, 但还是不支持索引操作

# 添加元素
s.add(5)
print(s)                                                    # {1, 2, 5, (3, 4)} 依旧只有一个 5，因为值唯一

# 删除元素
s.remove(2)                                                 # 删除指定元素，若该元素不存在，就报错

s.discard(6)                                                # 同样删除指定元素，但如果该元素不存在，也不会报错

a = s.pop()                                                 # 在集合中，pop是随机删除一个元素 (通常是内部哈希表的第一个位置) (集合无序性)
print(a)                                                    # 1  就算再尝试可能都是 1 ，因为插入顺序被保留，结果不会发生大变化了。。。表现为 “稳定删第一个”
                                                            # 注意：是插入顺序的第一，不是定义时的第一。

# 数学集合运算
a = {1,2,(3,4)}
b = {(3,4),5}
c = {3,(4,5)}

print(a | b)                                                # "|" 并集 {1, 2, (3, 4), 5} 合并集合，且去重(值唯一)
print(a | c)                                                # {1, 2, (4, 5), 3, (3, 4)} 元组是一个整体

print(a & b)                                                # "&" 交集 {(3, 4)} 只保留双方都有的值

print(b - a)                                                # "-" 差集 {5} 取出所有在 B 中但不在 A 中的元素。
print(a - b)                                                # {1，2}       取出所有在 A 中但不在 B 中的元素。

print(a ^ b)                                                # "^" 对称差集 {1, 5, 2} A 和 B 不同时有的元素，AB同时都有(3,4)，所以去掉了(3,4) 保留剩下的元素。


# 集合运用(去重)
a = [1,2,2,3,4,4,5]
a = list(set(a))                                            # 将 [列表] 转 {集合} 再转回 [列表]，完成去除重复值
print(a)                                                    # [1, 2, 3, 4, 5]



#-------------------------------------------------------------------------------------------------------------------------------------------------------------

# 扩展
from collections.abc import Iterable

# 类型转换
a = [1,2,3]

b = tuple(a)                                                  # tuple() 将类型转换成元组
c = set(a)                                                    # set()   将类型转换成集合
d = list(b)                                                   # list()  将类型转换成列表

# dict() 转字典则需要满足特定的格式 (需要成对的数据)
e = dict(enumerate(a))                                        # 使用索引充当另一对
print(e)                                                      # {0: 1, 1: 2, 2: 3}

# 验证
print(isinstance(d,list),isinstance(b,tuple),isinstance(c,set),isinstance(e,dict))                     # True True True True


# 列表推导式 [表达式 for 变量 in 迭代对象]

b = [i**2 for i in a]                                           # i**2 是表达式，每个从for循环 用 i 提取的数都要经过表达式。
print(b)                                                        # [1, 4, 9]

# 也可以加上条件判断 if
b = [i for i in range(10) if i % 2 == 0]
print(b)                                                        # [0, 2, 4, 6, 8]



# 生成器表达式 (generator)
c = (i for i in range(5))                                    # 这里生成的不是元组，而是一个单次迭代器(只能使用一次) 不会生成实际列表，直到调用时，才一个个产出元素，不存全量数据。且遍历一次之后自动"空壳"
print(isinstance(c, Iterable))                               # True

print(max(c))                                                # 第一次隐式遍历，每个元素被依次生成、比较、然后丢弃。最终得到最大值 4
# print(min(c))                                              # 第二次寻找最大值时直接报 值错误(ValueError) , c的序列为空
print(c is not None)                                         # True 虽然它虚了，但它仍然存在，想复用那就重新生成



# 集合推导式 (和列表推导式类似，但生成类型为集合，值唯一)
a = {i for i in range(5)} | {2,3,4,5}
print(a)                                                     # {0, 1, 2, 3, 4, 5}



# 字典推导式 {键 : 值 for 键值对 in 迭代对象 if 条件}
a = {i : i**2 for i in range(1,5) if i % 2 == 0}               # 偶数平方表
print(a)                                                       # {2: 4, 4: 16}


# 列表转字典
names = ["A","B","C"]
scores = [90,80,70]
b = {name:score for name,score in zip(names,scores)}           # zip(): 将两个可迭代对象合并为一对可迭代对象，如果两列长度不一样，会被截断成 最短 的长度。
print(b)                                                       # {'A': 90, 'B': 80, 'C': 70}


# 反转字典
c = {score:name for name,score in b.items()}                   # 或者 {score:name for name in a.keys() for score in a.values()} 只是说下 for循环也可以多对象同时进行...
print(c)                                                       # {90: 'A', 80: 'B', 70: 'C'}


# 嵌套字典(dict in dict)
d = {name: {"score": score, "pass": score >= 60} for name, score in b.items()}
print(d)
# {'A': {'score': 90, 'pass': True}, 'B': {'score': 80, 'pass': True}, 'C': {'score': 70, 'pass': True}}


# 一些容器(列表,元组)是可以直接比较的 (从左到右，依次比较每个同索引元素，一旦能决定大小就返回结果，后面不再比较。)
a = [1,2,3,5]                                                     # 是列表比列表，不能列表比元组
b = [1,2,4]
print(a < b)                                                      # True
